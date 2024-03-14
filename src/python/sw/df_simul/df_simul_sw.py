from typing import Tuple

import networkx as nx
from queue import Queue
from src.python.util.per_graph import PeRGraph
# from src.python.util.util import Util

class Node:
    def __init__(self, name: str):
        self.name: str = name
        self.in_queues: list[Queue] = []
        self.out_queues: list[Queue] = []
        self.has_data: bool = False
        self.exec_data: int = 0

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
            ret_value = True
            self.has_data = False

        # verify if inputs are ready to give data:
        for in_queue in self.in_queues:
            if in_queue.empty():
                return ret_value
        # verify if outputs are ready to receive data:
        for out_queue in self.out_queues:
            if not out_queue.empty():
                return ret_value

        # sum all inputs
        self.exec_data = self.has_data = True
        for in_queue in self.in_queues:
            self.exec_data += in_queue.get()
        return ret_value


class InputNode(Node):
    def __init__(self, name: str, n_data: int):
        super().__init__(name)
        self.exec_data: int = 0
        self.n_data: int = n_data
        self.done: bool = False

    def compute(self) -> bool:
        ret_value: bool = False
        if not self.done:
            # verify if outputs are ready to receive data:
            for out_queue in self.out_queues:
                if not out_queue.empty():
                    return ret_value

            ret_value = True
            for out_queue in self.out_queues:
                out_queue.put(self.exec_data)

            self.exec_data += 1
            if self.exec_data >= self.n_data:
                self.done = True
        return ret_value


class OutputNode(Node):
    def __init__(self, name: str):
        super().__init__(name)
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


class DfSimulSw:
    def __init__(self, per_graph: PeRGraph, output_base: str, n_data: int = 5000):
        self.per_graph: PeRGraph = per_graph
        self.output_base: str = output_base
        self.n_data: int = n_data
        self.g_with_regs: nx.DiGraph = self.add_regs()
        self.input_nodes: list[InputNode] = []
        self.output_nodes: list[OutputNode] = []
        self.dataflow: list[list[Node]] = self.create_dataflow()

    def run_simulation(self) -> list:
        input_nodes_done = False
        df_break = False
        counter_done = 0
        exec_counter = 0

        while not df_break and not input_nodes_done and counter_done < 5:
            df_break = True
            for stage in self.dataflow:
                for node in stage:
                    node_name = node.name
                    if node.compute():
                        df_break = False
            input_nodes_done = True
            for input_node in self.input_nodes:
                if not input_node.done:
                    input_nodes_done = False
                    break
            if df_break and input_nodes_done:
                counter_done += 1
            exec_counter += 1
        th: list = []
        for output_node in self.output_nodes:
            print(output_node.name,output_node.data,exec_counter)
            th.append([output_node.name, len(output_node.data) / exec_counter * 2 * 100])
        return th

    def add_regs(self) -> nx.DiGraph:
        df: nx.DiGraph = self.per_graph.g.copy()
        n_df: nx.DiGraph = df.copy()
        for edge in df.edges():
            if int(df.edges[edge]['weight']) > 0:
                # df.edges[edge]['label'] = df.edges[edge]['weight']
                src = edge[0]
                dst = edge[1]
                # port = int(df.edges[edge]['port'])
                for r in range(int(df.edges[edge]['weight'])):
                    idx = '%s_%s' % edge + '_%d' % r
                    n_df.add_node(idx)
                    nx.set_node_attributes(n_df, {idx: {'label': 'reg'}})
                    n_df.add_edge(src, idx)
                    nx.set_edge_attributes(n_df, {(src, idx): {'weight': 0}})
                    src = idx
                n_df.add_edge(src, dst)
                nx.set_edge_attributes(n_df, {(src, dst): {'weight': 0}})
                n_df.remove_edge(edge[0], edge[1])
        return n_df

    def find_nodes_level(self) -> tuple[dict, int]:
        g = self.g_with_regs
        level: int = 0
        queue: Queue = Queue()
        nodes_level: dict = {}
        for node in g.nodes:
            # node_name: str = str.lower(node)
            node_in_size: int = g.in_degree(node)
            if node_in_size == 0:
                queue.put([node, 0])
            else:
                continue
            while queue.qsize() > 0:
                n, l = queue.get()
                if n not in nodes_level.keys():
                    nodes_level[n] = l
                nodes_level[n] = max(l, nodes_level[n])
                level = max(level, l)
                try:
                    for succ in g._succ[n].keys():
                        # succ_name: str = str.lower(succ)
                        queue.put([succ, l + 1])
                except Exception as e:
                    a = 1
        return nodes_level, level + 1

    def create_dataflow(self) -> list[list[Node]]:
        nodes_levels, levels = self.find_nodes_level()
        g = self.g_with_regs
        dataflow: list[list[Node]] = [[] for _ in range(levels)]
        dfg_dic = {}
        visited: set = set()
        queue: Queue = Queue()
        for ini_node in g.nodes:
            # ini_node_name: str = str.lower(ini_node)
            if ini_node not in visited:
                queue.put(ini_node)
            while queue.qsize() > 0:
                no = queue.get()
                level = nodes_levels[no]
                node_in_size: int = g.in_degree(no)
                node_out_size: int = g.out_degree(no)
                if no not in visited:
                    node: Node = self.node_factory(no, node_in_size, node_out_size)
                    dfg_dic[no] = node
                    dataflow[level].append(node)
                    visited.add(no)
                node: Node = dfg_dic[no]
                for succ in g._succ[no].keys():
                    if succ == '24':
                        a = 1
                    # succ_name: str = str.lower(succ)
                    succ_in_size: int = g.in_degree(succ)
                    succ_out_size: int = g.out_degree(succ)
                    level = nodes_levels[succ]
                    if succ not in visited:
                        queue.put(succ)
                        succ_node: Node = self.node_factory(succ, succ_in_size, succ_out_size)
                        dfg_dic[succ] = succ_node
                        dataflow[level].append(succ_node)
                        visited.add(succ)
                    succ_node: Node = dfg_dic[succ]
                    succ_node.create_in_queue()
                    node.set_out_queue(succ_node.in_queues[-1])

        return dataflow

    def node_factory(self, name: str, n_inputs: int, n_outputs: int) -> Node:
        if n_inputs == 0:
            node: InputNode = InputNode(name, self.n_data)
            self.input_nodes.append(node)
            return node
        elif n_outputs == 0:
            node: OutputNode = OutputNode(name)
            self.output_nodes.append(node)
            return node
        else:
            return Node(name)

    # TODO implementar
    # Comentei pra resolver mais rápido o erro de import circular
    # def write_output_result(self, rslt: str):
    #     lines = rslt.split('\n')

    #     th = 0.0

    #     for line in lines:
    #         if 'throughput' in line:
    #             th = float(line.split(':')[2].replace(' ', '').replace('%', ''))
    #             break

    #     simul_result = {
    #         'benchmark': self.per_graph.dot_name,
    #         'throughput': th
    #     }
        # Util.save_json(self.result_path, self.result_file, simul_result)
