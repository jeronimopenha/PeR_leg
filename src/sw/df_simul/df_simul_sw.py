import networkx as nx
from queue import Queue
from src.util.per_graph import PeRGraph


class DfSimulHw:
    def __init__(self, per_graph: PeRGraph, output_base: str):
        self.per_graph = per_graph
        self.df: nx.DiGraph = self.add_regs()
        self.test_bench: Module = self.make_test_bench()

    def start_simulation(self):
        self.test_bench.to_verilog(self.verilog_file)
        sim = simulation.Simulator(self.test_bench, sim='iverilog')
        print('Starting simulation')
        rslt = sim.run(outputfile=self.output_file)
        print('Simulation done')
        self.write_output_result(rslt)
        os.remove(self.output_file)

    def write_output_result(self, rslt: str):
        lines = rslt.split('\n')

        th = 0.0

        for line in lines:
            if 'throughput' in line:
                th = float(line.split(':')[2].replace(' ', '').replace('%', ''))
                break

        simul_result = {
            'benchmark': self.per_graph.dot_name,
            'throughput': th
        }
        Util.save_json(self.result_path, self.result_file, simul_result)

    def add_regs(self) -> nx.DiGraph:
        df: nx.DiGraph = self.per_graph.g.copy()
        n_df: nx.DiGraph = df.copy()
        for edge in df.edges():
            if int(df.edges[edge]['w']) > 0:
                df.edges[edge]['label'] = df.edges[edge]['w']
                src = edge[0]
                dst = edge[1]
                port = int(df.edges[edge]['port'])
                for r in range(int(df.edges[edge]['w'])):
                    idx = '%s_%s' % edge + '_%d' % r
                    n_df.add_node(idx)
                    nx.set_node_attributes(n_df, {idx: {'label': 'reg', 'op': 'reg'}})
                    n_df.add_edge(src, idx)
                    nx.set_edge_attributes(n_df, {(src, idx): {'port': 0, 'w': 0}})
                    src = idx
                n_df.add_edge(src, dst)
                nx.set_edge_attributes(n_df, {(src, dst): {'port': port, 'w': 0}})
                n_df.remove_edge(edge[0], edge[1])
        return n_df

    def make_dataflow(self):
        df = self.df
        m = Module(df.name)
        data_width = m.Parameter('data_width', 32)
        clk = m.Input('clk')
        rst = m.Input('rst')
        wires = self.create_wires(m)
        operator = self.make_async_operator()
        for no in df.nodes:
            op = str.lower(df.nodes[no]['op'])
            immediate = self.get_immediate(df.nodes[no])
            input_size = df.in_degree(no)
            output_size = df.out_degree(no)
            if op == 'in':
                input_size += 1
            if op == 'out':
                output_size += 1

            req_l, ack_l, din, req_r, ack_r, dout = self.create_con_node(no)
            param = [('data_width', data_width),
                     ('op', op),
                     ('immediate', immediate),
                     ('input_size', input_size),
                     ('output_size', output_size)
                     ]
            con = [('clk', clk),
                   ('rst', rst),
                   ('req_l', req_l),
                   ('ack_l', ack_l),
                   ('req_r', req_r),
                   ('ack_r', ack_r),
                   ('din', din),
                   ('dout', dout)]
            m.Instance(operator, '%s_%s' % (op, no), param, con)

        return m

    
class Node:
    def __init__(self):
        self.in_queues: list[Queue] = []
        self.out_queues: list[Queue] = []
        self.exec_data: int = 0
        self.has_data: bool = False

    def get_n_in_queues(self) -> int:
        if self.in_queues:
            return len(self.in_queues)
        return 0

    def create_in_queue(self):
        self.in_queues.append(Queue(1))

    def set_out_queue(self, queue: Queue):
        self.out_queues.append(queue)

    def compute(self) -> bool:
        ret_value: bool = False
        if self.has_data:
            # enqueue all outputs
            for out_queue in self.out_queues:
                out_queue.put(self.exec_data)
            self.has_data = False
            ret_value = True

        # verify if inputs are ready to give data:
        for in_queue in self.in_queues:
            if in_queue.empty():
                return ret_value
        # verify if outputs are ready to receive data:
        for out_queue in self.out_queues:
            if not out_queue.empty():
                return ret_value
        # sum all inputs
        self.exec_data = 0
        self.has_data = True
        for in_queue in self.in_queues:
            self.exec_data += in_queue.get()
        return ret_value


class InputNode(Node):
    def __init__(self, n_data: int):
        super().__init__()
        self.n_data: int = n_data
        self.done: bool = False

    def compute(self) -> bool:
        ret_value: bool = False
        if self.has_data:
            # enqueue all outputs
            for out_queue in self.out_queues:
                out_queue.put(self.exec_data)
            self.has_data = False
            ret_value = True

        if not self.done:
            # verify if outputs are ready to receive data:
            for out_queue in self.out_queues:
                if not out_queue.empty():
                    return ret_value
            # sum all inputs
            self.exec_data += 1
            self.has_data = True

            if self.exec_data >= self.n_data:
                self.done = True

        return ret_value


class OutputNode(Node):
    def __init__(self):
        super().__init__()
        self.data: list = []

    def compute(self) -> bool:
        # verify if inputs are ready to give data:
        for in_queue in self.in_queues:
            if in_queue.empty():
                return False
        # sum all inputs
        exec_data = 0
        for in_queue in self.in_queues:
            exec_data += in_queue.get()
        self.data.append(exec_data)
        return True
