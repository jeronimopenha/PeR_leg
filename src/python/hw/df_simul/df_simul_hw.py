from veriloggen import *
import networkx as nx
from src.python.util.util import Util

from src.python.util.per_graph import PeRGraph


class DfSimulHw:
    def __init__(self, per_graph: PeRGraph, output_base: str):
        self.per_graph = per_graph
        self.verilog_file = f'{output_base}/verilog/{self.per_graph.dot_name.replace(".", "_")}.v'
        self.output_file = f'{output_base}/{self.per_graph.dot_name.replace(".", "_")}.out'
        self.result_path = f'{output_base}/results'
        self.result_file = f'{self.per_graph.dot_name.replace(".", "_")}.json'
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

    def make_test_bench(self) -> Module:
        df = self.df
        dataflow = self.make_dataflow()
        m = Module(self.per_graph.dot_name.replace(".", "_"))
        data_width = m.Localparam('data_width', 32)
        fail_rate_producer = m.Localparam('fail_rate_producer', 0)
        fail_rate_consumer = m.Localparam('fail_rate_consumer', 0)
        is_const = m.Localparam('is_const', 'false')
        initial_value = m.Localparam('initial_value', 0)

        max_data_size = m.Localparam('max_data_size', 5000)

        clk = m.Reg('clk')
        rst = m.Reg('rst')

        df_ports = dataflow.get_ports()
        ports = m.get_vars()
        for p in df_ports:
            if p not in ports:
                m.Wire(p, df_ports[p].width)

        ports = m.get_vars()

        n_in = 0
        n_out = 0
        for no in df.nodes:
            op = str.lower(df.nodes[no]['op'])
            if op == 'in':
                n_in += 1
            elif op == 'out':
                n_out += 1

        count_producer = m.Wire('count_producer', 32, n_in)
        count_consumer = m.Wire('count_consumer', 32, n_out)
        count_clock = m.Real('count_clock', 32)

        m.EmbeddedCode('')
        consumers_done = m.Wire('consumers_done', n_out)
        done = m.Wire('done')
        for i in range(n_out):
            consumers_done[i].assign(count_consumer[i] >= max_data_size)

        done.assign(Uand(consumers_done))

        simulation.setup_clock(m, clk, hperiod=1)
        simulation.setup_reset(m, rst, period=1)
        # simulation.setup_waveform(m)

        i = m.Integer('i')

        m.Always(Posedge(clk))(
            If(rst)(
                count_clock(0)
            ),
            count_clock.inc(),
            If(done)(
                For(i(0), i < n_out, i.inc())(
                    Display(self.per_graph.dot_name.replace(".", "_") + " throughput: %d : %5.2f%%", i,
                            Mul(100.0, (count_consumer[i] / (count_clock / 4.0)))),

                ),
                Finish()
            )
        )
        p = self.make_producer()
        c = self.make_consumer()
        c_in = 0
        c_out = 0
        for no in df.nodes:
            op = str.lower(df.nodes[no]['op'])
            if op == 'in':
                param = [
                    ('producer_id', int(no)),
                    ('data_width', data_width),
                    ('fail_rate', fail_rate_producer),
                    ('initial_value', initial_value),
                    ('is_const', is_const)
                ]
                con = [
                    ('clk', clk),
                    ('rst', rst),
                    ('req', ports['din_req_%s' % no]),
                    ('ack', ports['din_ack_%s' % no]),
                    ('dout', ports['din_%s' % no]),
                    ('count', count_producer[c_in])
                ]
                m.Instance(p, p.name + '_%s' % no, param, con)
                c_in += 1
            elif op == 'out':
                param = [
                    ('consumer_id', int(no)),
                    ('data_width', data_width),
                    ('fail_rate', fail_rate_consumer)
                ]
                con = [
                    ('clk', clk),
                    ('rst', rst),
                    ('req', ports['dout_req_%s' % no]),
                    ('ack', ports['dout_ack_%s' % no]),
                    ('din', ports['dout_%s' % no]),
                    ('count', count_consumer[c_out])
                ]
                m.Instance(c, c.name + '_%s' % no, param, con)
                c_out += 1

        m.Instance(dataflow, dataflow.name,
                   dataflow.get_params(), dataflow.get_ports())

        return m

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

    def create_wires(self, m: Module()) -> dict:
        df = self.df
        data_width = m.get_params()['data_width']
        wires = {}
        for no in df.nodes:
            op = str.lower(df.nodes[no]['op'])
            for n in df.successors(no):
                req_r = m.Wire('req_%s_%s' % (no, n))
                wires[req_r.name] = req_r
            if op == 'in':
                req_r = m.Output('din_req_%s' % no)
                ack_r = m.Input('din_ack_%s' % no)
                d = m.Input('din_%s' % no, data_width)
                wires[req_r.name] = req_r
                wires[ack_r.name] = ack_r
                wires[d.name] = d
                ack_r = m.Wire('ack_%s' % no)
                d = m.Wire('d%s' % no, data_width)
                wires[ack_r.name] = ack_r
                wires[d.name] = d
            elif op == 'out':
                parent = [n for n in df.predecessors(no)][0]
                req_r = m.Input('dout_req_%s' % no)
                ack_r = m.Output('dout_ack_%s' % no)
                d = m.Output('dout_%s' % no, data_width)
                wires['req_%s' % parent] = req_r
                wires['ack_%s' % parent] = ack_r
                wires['d%s' % parent] = d
            else:
                ack_r = m.Wire('ack_%s' % no)
                d = m.Wire('d%s' % no, data_width)
                wires[ack_r.name] = ack_r
                wires[d.name] = d

        return wires

    def make_async_operator(self) -> Module():
        m = Module('async_operator')
        data_width = m.Parameter('data_width', 32)
        op = m.Parameter('op', 'reg')
        immediate = m.Parameter('immediate', data_width)
        input_size = m.Parameter('input_size', 1)
        output_size = m.Parameter('output_size', 1)

        clk = m.Input('clk')
        rst = m.Input('rst')
        req_l = m.OutputReg('req_l', input_size)
        ack_l = m.Input('ack_l', input_size)
        req_r = m.Input('req_r', output_size)
        ack_r = m.Output('ack_r')
        din = m.Input('din', Mul(data_width, input_size))
        dout = m.Output('dout', data_width)

        din_r = m.Reg('din_r', Mul(data_width, input_size))
        has_all = m.Wire('has_all')
        req_r_all = m.Wire('req_r_all')
        ack_r_all = m.Reg('ack_r_all', output_size)
        has = m.Reg('has', input_size)

        i = m.Integer('i')
        g = m.Genvar('g')

        has_all.assign(Uand(has))
        req_r_all.assign(Uand(req_r))
        ack_r.assign(Uand(ack_r_all))
        m.Always(Posedge(clk))(
            If(rst)(
                has(Repeat(Int(0, 1, 2), input_size)),
                ack_r_all(Repeat(Int(0, 1, 2), output_size)),
                req_l(Repeat(Int(0, 1, 2), input_size))
            ).Else(
                For(i(0), i < input_size, i.inc())(
                    If(~has[i] & ~req_l[i])(
                        req_l[i](Int(1, 1, 2))
                    ),
                    If(ack_l[i])(
                        has[i](Int(1, 1, 2)),
                        req_l[i](Int(0, 1, 2))
                    )
                ),
                If(has_all & req_r_all)(
                    ack_r_all(Repeat(Int(1, 1, 2), output_size)),
                    has(Repeat(Int(0, 1, 2), input_size)),
                ),
                If(~has_all)(
                    ack_r_all(Repeat(Int(0, 1, 2), output_size)),
                )
            )
        )
        genfor = m.GenerateFor(g(0), g < input_size, g.inc(), 'rcv')
        genfor.Always(Posedge(ack_l[g]))(
            din_r[Mul(data_width, g):Mul(data_width, g + 1)
            ](din[Mul(data_width, g):Mul(data_width, g + 1)])
        )

        operator = self.make_operator()
        param = [('input_size', input_size), ('op', op),
                 ('immediate', immediate), ('data_width', data_width)]
        con = [('din', din_r), ('dout', dout)]
        m.Instance(operator, 'operator', param, con)

        return m

    def make_operator(self) -> Module():
        m = Module('operator')
        fanin = m.Parameter('input_size', 1)
        op = m.Parameter('op', 'reg')
        immediate = m.Parameter('immediate', 0)
        data_width = m.Parameter('data_width', 32)

        din = m.Input('din', Mul(data_width, fanin))
        dout = m.Output('dout', data_width)

        unary_code = 'assign dout = din%simmediate;'
        binary_code = 'assign dout = din[data_width-1:0]%sdin[data_width*2-1:data_width];'
        ternary_code = 'assign dout = din[data_width-1:0]%sdin[data_width*2-1:data_width]%sdin[data_width*3-1:data_width*2];'

        genif = m.GenerateIf(fanin == 1, 'gen_op')
        genif.GenerateIf(OrList(Eql(op, "reg"), Eql(op, "in"), Eql(
            op, "out"))).EmbeddedCode('assign dout = din;')
        genif.GenerateIf(Eql(op, "addi")).EmbeddedCode(unary_code % '+')
        genif.GenerateIf(Eql(op, "subi")).EmbeddedCode(unary_code % '-')
        genif.GenerateIf(Eql(op, "muli")).EmbeddedCode(unary_code % '*')
        genif = genif.Else.GenerateIf(fanin == 2)
        genif.GenerateIf(Eql(op, "add")).EmbeddedCode(binary_code % '+')
        genif.GenerateIf(Eql(op, "sub")).EmbeddedCode(binary_code % '-')
        genif.GenerateIf(Eql(op, "mul")).EmbeddedCode(binary_code % '*')
        genif = genif.Else.GenerateIf(fanin == 3)
        genif.GenerateIf(Eql(op, "add")).EmbeddedCode(ternary_code % ('+', '+'))
        genif.GenerateIf(Eql(op, "sub")).EmbeddedCode(ternary_code % ('-', '-'))
        genif.GenerateIf(Eql(op, "mul")).EmbeddedCode(ternary_code % ('*', '*'))

        return m

    def get_immediate(self, no: dict) -> int:
        immediate = 0
        operators = ['addi', 'subi', 'muli']
        name = str.lower(no['op'])
        if name in operators:
            immediate = int(no['value'])
        return immediate

    def create_con_node(self, no: str) -> list:
        df = self.df
        din = ''
        req_l = ''
        ack_l = ''
        req_r = ''
        dout = ''
        ack_r = ''

        if df.nodes[no]['op'] == 'in':
            req_l = 'din_req_%s' % no
            ack_l = 'din_ack_%s' % no
            ack_r = 'ack_%s' % no
            din = 'din_%s' % no
            dout = 'd%s' % no
            req_r = '{'
            for d in df.successors(no):
                req_r += 'req_%s_%s, ' % (no, d)
            req_r = req_r[:-2]
            req_r += '}'
        elif df.nodes[no]['op'] == 'out':
            req_r = 'dout_req_%s' % no
            ack_r = 'dout_ack_%s' % no
            dout = 'dout_%s' % no
            for d in df.predecessors(no):
                req_l = 'req_%s_%s' % (d, no)
                ack_l = 'ack_%s' % d
                din = 'd%s' % d
                break
        else:
            req_l = '{'
            ack_l = '{'
            din = '{'
            req_r = '{'
            ack_r = ''
            dout = ''
            for d in df.successors(no):
                req_r += 'req_%s_%s, ' % (no, d)
            req_r = req_r[:-2]
            req_r += '}'
            ack_r += 'ack_%s' % no
            dout += 'd%s' % no
            portsl = [0 for _ in df.predecessors(no)]
            for d in df.predecessors(no):
                portsl[int(df.edges[(d, no)]['port'])] = d
                req_l += 'req_%s_%s, ' % ('%s', no)
                ack_l += 'ack_%s, '
                din += 'd%s, '
            req_l = req_l[:-2]
            ack_l = ack_l[:-2]
            din = din[:-2]
            req_l += '}'
            ack_l += '}'
            din += '}'
            portsl = tuple(reversed(portsl))
            req_l = req_l % portsl
            ack_l = ack_l % portsl
            din = din % portsl

        req_l = EmbeddedCode(req_l)
        ack_l = EmbeddedCode(ack_l)
        din = EmbeddedCode(din)
        req_r = EmbeddedCode(req_r)
        ack_r = EmbeddedCode(ack_r)
        dout = EmbeddedCode(dout)
        con = req_l, ack_l, din, req_r, ack_r, dout

        return con

    def make_producer(self) -> Module():
        m = Module('producer')
        producer_id = m.Parameter('producer_id', 0)
        data_width = m.Parameter('data_width', 8)
        fail_rate = m.Parameter('fail_rate', 0)
        is_const = m.Parameter('is_const', 'false')
        initial_value = m.Parameter('initial_value', 0)
        clk = m.Input('clk')
        rst = m.Input('rst')
        req = m.Input('req')
        ack = m.OutputReg('ack')
        dout = m.OutputReg('dout', data_width)
        count = m.OutputReg('count', 32)

        dout_next = m.Reg('dout_next', data_width)
        stop = m.Reg('stop')
        randd = m.Real('randd')
        m.Always(Posedge(clk))(
            If(rst)(
                dout(initial_value),
                dout_next(initial_value),
                ack(0),
                count(0),
                stop(0),
                randd(EmbeddedCode('$abs($random%101)+1')),
            ).Else(
                ack(0),
                randd(EmbeddedCode('$abs($random%101)+1')),
                stop(Mux(randd > fail_rate, 0, 1)),
                # If(ack)(
                #    Write("p_%d,%d\\n",producer_id,dout)
                # ),
                If(req & ~ack & Not(stop))(
                    ack(1),
                    dout(dout_next),
                    If(is_const == "false")(
                        dout_next.inc()
                    ),
                    count.inc()
                )
            )
        )

        return m

    def make_consumer(self) -> Module():
        m = Module('consumer')
        consumer_id = m.Parameter('consumer_id', 0)
        data_width = m.Parameter('data_width', 8)
        fail_rate = m.Parameter('fail_rate', 0)
        clk = m.Input('clk')
        rst = m.Input('rst')
        req = m.OutputReg('req')
        ack = m.Input('ack')
        din = m.Input('din', data_width)
        count = m.OutputReg('count', 32)
        stop = m.Reg('stop')
        randd = m.Real('randd')
        m.Always(Posedge(clk))(
            If(rst)(
                req(0),
                count(0),
                stop(0),
                randd(EmbeddedCode('$abs($random%101)+1'))
            ).Else(
                req(0),
                randd(EmbeddedCode('$abs($random%101)+1')),
                stop(Mux(randd > fail_rate, 0, 1)),
                If(Not(stop))(
                    req(1)
                ),
                If(ack)(
                    count.inc(),
                    # Write("c_%d, %d\\n", consumer_id, din)
                )
            )
        )
        return m
