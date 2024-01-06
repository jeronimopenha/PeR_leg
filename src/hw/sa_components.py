from math import ceil, dist, log2, sqrt

from numpy import base_repr
from veriloggen import *
import src.util.util as _u
from src.util.sagraph import SaGraph


class SAComponents:
    _instance = None

    def __init__(
            self,
            sa_graph: SaGraph,
            base_path: str,
            parent_name: str,
            n_neighbors: int = 4,
            align_bits: int = 8,
    ):
        self.sa_graph = sa_graph
        self.base_path = base_path
        self.parent_name = parent_name
        self.n_cells = sa_graph.n_cells
        self.n_cells_sqrt = sa_graph.n_cells_sqrt
        self.n_neighbors = n_neighbors
        self.align_bits = align_bits

        self.cell_bits = ceil(log2(self.n_cells))
        self.node_bits = self.cell_bits
        self.lines = self.columns = int(sqrt(self.n_cells))
        self.dist_bits = self.cell_bits + ceil(log2(self.n_neighbors * 2))
        self.lc_bits = ceil(log2(self.lines)) * 2

        self.cache = {}

    def create_memory_2r_1w(self, width, depth) -> Module:
        name = 'mem_2r_1w_width%d_depth%d' % (width, depth)
        if name in self.cache.keys():
            return self.cache[name]

        m = Module(name)
        READ_F = m.Parameter('READ_F', 0)
        INIT_FILE = m.Parameter('INIT_FILE', 'mem_file.txt')
        WRITE_F = m.Parameter('WRITE_F', 0)
        OUTPUT_FILE = m.Parameter('OUTPUT_FILE', 'mem_out_file.txt')

        clk = m.Input('clk')
        rd = m.Input('rd')
        rd_addr0 = m.Input('rd_addr0', depth)
        rd_addr1 = m.Input('rd_addr1', depth)
        out0 = m.Output('out0', width)
        out1 = m.Output('out1', width)

        wr = m.Input('wr')
        wr_addr = m.Input('wr_addr', depth)
        wr_data = m.Input('wr_data', width)

        # m.EmbeddedCode(
        #    '(*rom_style = "block" *) reg [%d-1:0] mem[0:2**%d-1];' % (width, depth))
        # m.EmbeddedCode('/*')
        mem = m.Reg('mem', width, Power(2, depth))
        # m.EmbeddedCode('*/')

        out0.assign(Mux(rd, mem[rd_addr0], Int(0, width, 10)))
        out1.assign(Mux(rd, mem[rd_addr1], Int(0, width, 10)))

        m.Always(Posedge(clk))(
            If(wr)(
                mem[wr_addr](wr_data)
            ),
        )

        m.EmbeddedCode('//synthesis translate_off')
        m.Always(Posedge(clk))(
            If(AndList(wr, WRITE_F))(
                Systask('writememb', OUTPUT_FILE, mem)
            ),
        )
        m.EmbeddedCode('//synthesis translate_on')

        m.Initial(
            If(READ_F)(
                Systask('readmemb', INIT_FILE, mem),
            )
        )
        self.cache[name] = m
        return m

    def create_lc_table(self) -> Module:
        # LC table.
        # Finds the line/column values for each cell
        n_cells = self.n_cells
        cell_bits = self.cell_bits
        lines = self.lines
        columns = self.columns
        lc_bits = self.lc_bits

        name = 'lc_table_%d_%d' % (lines, columns)
        if name in self.cache.keys():
            return self.cache[name]

        m = Module(name)

        ca = m.Input('ca', cell_bits)
        cb = m.Input('cb', cell_bits)
        lca = m.Output('lca', lc_bits)
        lcb = m.Output('lcb', lc_bits)

        lc_table = m.Wire('lc_table', lc_bits, n_cells)

        lca.assign(lc_table[ca])
        lcb.assign(lc_table[cb])

        counter = 0
        for line in range(lines):
            for column in range(columns):
                w = lc_bits // 2
                lc_table[counter].assign(Cat(Int(line, w, 10), Int(column, w, 10)))
                counter += 1

        _u.initialize_regs(m)
        self.cache[name] = m
        return m

    def create_distance_table(self) -> Module:
        # manhattan
        lines = self.lines
        columns = self.columns
        dist_bits = self.dist_bits
        lc_bits = self.lc_bits
        w = lc_bits // 2

        name = 'distance_table_%d_%d' % (lines, columns)
        if name in self.cache.keys():
            return self.cache[name]

        m = Module(name)

        opa0 = m.Input('opa0', lc_bits)
        opa1 = m.Input('opa1', lc_bits)
        opav = m.Input('opav')
        opb0 = m.Input('opb0', lc_bits)
        opb1 = m.Input('opb1', lc_bits)
        opbv = m.Input('opbv')
        da = m.Output('da', dist_bits)
        db = m.Output('db', dist_bits)

        dist_table = m.Wire('dist_table', dist_bits, Power(2, lc_bits))

        da_t = m.Wire('da_t', dist_bits)
        db_t = m.Wire('db_t', dist_bits)

        m.EmbeddedCode('')
        da_t.assign(dist_table[Cat(opa1[:w], opa0[:w])] +
                    dist_table[Cat(opa1[w:], opa0[w:])])
        db_t.assign(dist_table[Cat(opb1[:w], opb0[:w])] +
                    dist_table[Cat(opb1[w:], opb0[w:])])

        m.EmbeddedCode('')
        da.assign(Mux(opav, da_t, 0))
        db.assign(Mux(opbv, db_t, 0))

        m.EmbeddedCode('')
        for i in range(lines):
            for j in range(lines):
                dist_table[(i << w) | j].assign(abs(i - j))

        _u.initialize_regs(m)
        self.cache[name] = m
        return m

    def create_sa_fsm_single_thread(self):
        n_cells = self.n_cells
        n_cells_sqrt = self.n_cells_sqrt
        n_neighbors = self.n_neighbors
        cell_bits = self.cell_bits
        node_bits = self.node_bits
        lc_bits = self.lc_bits
        dist_bits = self.dist_bits
        base_path = self.base_path
        parent_name = self.parent_name

        name = 'sa_single_%dcells' % n_cells
        if name in self.cache.keys():
            return self.cache[name]

        m = Module(name)

        clk = m.Input('clk')
        rst = m.Input('rst')
        start = m.Input('start')
        done = m.Input('done')

        m.EmbeddedCode('// SA single thread states declaration')
        fsm_sa = m.Reg('fsm_sa', 4)
        SELECT_CELLS = m.Localparam('SELECT_CELLS', Int(0, fsm_sa.width, 10))
        CELL_TO_NODES = m.Localparam('CELL_TO_NODES', Int(1, fsm_sa.width, 10))
        NEIGHBORHOOD = m.Localparam('NEIGHBORHOOD', Int(2, fsm_sa.width, 10))
        NODES_TO_CELL = m.Localparam('NODES_TO_CELL', Int(3, fsm_sa.width, 10))
        LINE_COLUMN_FINDER = m.Localparam('LINE_COLUMN_FINDER', Int(4, fsm_sa.width, 10))
        DISTANCE_CALCULATOR = m.Localparam('DISTANCE_CALCULATOR', Int(5, fsm_sa.width, 10))
        SUM_REDUCTION = m.Localparam('SUM_REDUCTION', Int(6, fsm_sa.width, 10))
        DECISION = m.Localparam('DECISION', Int(7, fsm_sa.width, 10))
        CHANGES = m.Localparam('CHANGES', Int(8, fsm_sa.width, 10))
        END = m.Localparam('END', Int(9, fsm_sa.width, 10))
        m.EmbeddedCode('// #####')

        m.EmbeddedCode('')
        m.EmbeddedCode('// select cells stage variables')
        ca = m.Reg('ca', cell_bits)
        cb = m.Reg('cb', cell_bits)
        m.EmbeddedCode('// #####')

        m.EmbeddedCode('')
        m.EmbeddedCode('// cell to nodes stage variables')
        na = m.Reg('na', node_bits)
        na_v = m.Reg('na_v')
        nb = m.Reg('nb', node_bits)
        nb_v = m.Reg('nb_v')
        na_t = m.Wire('na_t', node_bits)
        na_v_t = m.Wire('na_v_t')
        nb_t = m.Wire('nb_t', node_bits)
        nb_v_t = m.Wire('nb_v_t')
        m.EmbeddedCode('// #####')

        m.EmbeddedCode('')
        m.EmbeddedCode('// neighborhood stage variables')
        va = m.Reg('va', node_bits * n_neighbors)
        va_v = m.Reg('va_v', n_neighbors)
        vb = m.Reg('vb', node_bits * n_neighbors)
        vb_v = m.Reg('vb_v', n_neighbors)
        va_t = m.Wire('va_t', node_bits * n_neighbors)
        va_v_t = m.Wire('va_v_t', n_neighbors)
        va_v_m = m.Wire('va_v_m', n_neighbors)
        vb_t = m.Wire('vb_t', node_bits * n_neighbors)
        vb_v_t = m.Wire('vb_v_t', n_neighbors)
        vb_v_m = m.Wire('vb_v_m', n_neighbors)

        m.EmbeddedCode('')
        m.EmbeddedCode('//here we guarantee that only valid nodes can give neighbors ')
        va_v_t.assign(Mux(na_v, va_v_m, Int(0, n_neighbors, 2)))
        vb_v_t.assign(Mux(nb_v, vb_v_m, Int(0, n_neighbors, 2)))
        m.EmbeddedCode('// #####')

        m.EmbeddedCode('')
        m.EmbeddedCode('// node to cell stage variables')
        cva_v = m.Reg('cva_v', n_neighbors)
        cva = m.Reg('cva', cell_bits * n_neighbors)
        cvb_v = m.Reg('cvb_v', n_neighbors)
        cvb = m.Reg('cvb', cell_bits * n_neighbors)
        cva_v_t = m.Wire('cva_v_t', n_neighbors)
        cva_t = m.Wire('cva_t', cell_bits * n_neighbors)
        cvb_v_t = m.Wire('cvb_v_t', n_neighbors)
        cvb_t = m.Wire('cvb_t', cell_bits * n_neighbors)

        m.EmbeddedCode('')
        m.EmbeddedCode('// This is only for legibility')
        cva_v_t.assign(va_v)
        cvb_v_t.assign(vb_v)
        m.EmbeddedCode('// #####')

        m.EmbeddedCode('')
        m.EmbeddedCode('// line column finder stage variables')
        lca = m.Reg('lca', lc_bits)
        lcb = m.Reg('lcb', lc_bits)
        lcva = m.Reg('lcva', lc_bits * n_neighbors)
        lcva_v = m.Reg('lcva_v', n_neighbors)
        lcvb = m.Reg('lcvb', lc_bits * n_neighbors)
        lcvb_v = m.Reg('lcvb_v', n_neighbors)

        lca_t = m.Wire('lca_t', lc_bits)
        lcb_t = m.Wire('lcb_t', lc_bits)
        lcva_t = m.Wire('lcva_t', lc_bits * n_neighbors)
        lcvb_t = m.Wire('lcvb_t', lc_bits * n_neighbors)
        m.EmbeddedCode('// #####')

        m.EmbeddedCode('')  # TODO
        m.EmbeddedCode('// Distance calculator stage variables')
        dvac = m.Reg('dvac', n_neighbors * dist_bits)
        dvbc = m.Reg('dvbc', n_neighbors * dist_bits)
        m.EmbeddedCode('// #####')

        m.EmbeddedCode('')
        m.EmbeddedCode('// SA single thread FSM')
        m.Always(Posedge(clk))(
            If(rst)(
                ca(Int(0, ca.width, 10)),
                cb(Int(0, cb.width, 10)),
                na(Int(0, na.width, 10)),
                na_v(Int(0, 1, 10)),
                nb(Int(0, nb.width, 10)),
                nb_v(Int(0, 1, 10)),
                va(Int(0, va.width, 10)),
                va_v(Int(0, va_v.width, 10)),
                vb(Int(0, vb.width, 10)),
                vb_v(Int(0, vb_v.width, 10)),
                lca(Int(0, lca.width, 10)),
                lcb(Int(0, lcb.width, 10)),
                lcva(Int(0, lcva.width, 10)),
                lcva_v(Int(0, lcva_v.width, 10)),
                lcvb(Int(0, lcvb.width, 10)),
                lcvb_v(Int(0, lcvb_v.width, 10)),
                fsm_sa(CELL_TO_NODES)
            ).Elif(start)(
                Case(fsm_sa)(
                    When(SELECT_CELLS)(
                        If(ca == Int(n_cells_sqrt, ca.width, 10))(
                            ca(Int(0, ca.width, 10)),
                            If(cb == Int(n_cells_sqrt, cb.width, 10))(
                                cb(Int(0, cb.width, 10)),
                                fsm_sa(END)
                            ).Else(
                                cb(cb + Int(1, cb.width, 10)),
                                fsm_sa(CELL_TO_NODES),
                            )
                        ).Else(
                            ca(ca + Int(1, ca.width, 10)),
                            fsm_sa(CELL_TO_NODES),
                        ),
                    ),
                    When(CELL_TO_NODES)(
                        If(Uand(Cat(~na_v_t, ~nb_v_t)))(
                            fsm_sa(SELECT_CELLS),
                        ).Else(
                            na(na_t),
                            na_v(na_v_t),
                            nb(nb_t),
                            nb_v(nb_v_t),
                            fsm_sa(NEIGHBORHOOD),
                        ),
                    ),
                    When(NEIGHBORHOOD)(
                        va(va_t),
                        va_v(va_v_t),
                        vb(vb_t),
                        vb_v(vb_v_t),
                        fsm_sa(NODES_TO_CELL),
                    ),
                    When(NODES_TO_CELL)(
                        cva_v(cva_v_t),
                        cva(cva_t),
                        cvb_v(cvb_v_t),
                        cvb(cvb),
                        fsm_sa(LINE_COLUMN_FINDER)
                    ),
                    When(LINE_COLUMN_FINDER)(
                        lca(lca_t),
                        lcb(lcb_t),
                        lcva(lcva_t),
                        lcva_v(cva_v),
                        lcvb(lcvb_t),
                        lcvb_v(cvb_v),
                        fsm_sa(DISTANCE_CALCULATOR),
                    ),
                    When(DISTANCE_CALCULATOR)(  # TODO
                        fsm_sa(SUM_REDUCTION)
                    ),
                    When(SUM_REDUCTION)(
                        fsm_sa(DECISION)
                    ),
                    When(DECISION)(
                        fsm_sa(CHANGES),
                        fsm_sa(SELECT_CELLS)
                    ),
                    When(CHANGES)(
                        fsm_sa(SELECT_CELLS)
                    ),
                    When(END)(
                        fsm_sa(END)
                    ),
                )
            )
        )

        m.EmbeddedCode('// cell to nodes stage memory instantiation')
        par = [
            ('READ_F', 1),
            ('INIT_FILE', base_path + '/verilog/' + parent_name + '_c_n.rom'),
            ('WRITE_F', 1),
            ('OUTPUT_FILE', base_path + '/verilog/' + parent_name + '_c_n_out.rom')
        ]
        con = [
            ('clk', clk),
            ('rd', Int(1, 1, 10)),
            ('rd_addr0', ca),
            ('rd_addr1', cb),
            ('out0', Cat(na_v_t, na_t)),
            ('out1', Cat(nb_v_t, nb_t)),
            ('wr', Int(0, 1, 10)),  # TODO
            ('wr_addr', Int(0, cell_bits, 10)),  # TODO
            ('wr_data', Int(0, node_bits + 1, 10)),  # TODO
        ]
        aux = self.create_memory_2r_1w(node_bits + 1, cell_bits)
        m.Instance(aux, aux.name, par, con)
        m.EmbeddedCode('// #####')

        m.EmbeddedCode('')
        m.EmbeddedCode('// neighborhood stage memory instantiation')
        for i in range(n_neighbors):
            par = [
                ('READ_F', 1),
                ('INIT_FILE', base_path + '/verilog/' + parent_name + '_n%d.rom' % i),
                ('WRITE_F', 0)
            ]
            con = [
                ('clk', clk),
                ('rd', Int(1, 1, 10)),
                ('rd_addr0', na),
                ('rd_addr1', nb),
                ('out0', Cat(va_v_m[i], va_t[node_bits * i:node_bits * (i + 1)])),
                ('out1', Cat(vb_v_m[i], vb_t[node_bits * i:node_bits * (i + 1)])),
                ('wr', Int(0, 1, 10)),  # TODO
                ('wr_addr', Int(0, node_bits, 10)),  # TODO
                ('wr_data', Int(0, node_bits + 1, 10)),  # TODO
            ]
            aux = self.create_memory_2r_1w(node_bits + 1, node_bits)
            m.Instance(aux, '%s_%i' % (aux.name, i), par, con)
        m.EmbeddedCode('// #####')

        m.EmbeddedCode('')
        m.EmbeddedCode('// node to cell stage memory instantiation')
        for i in range(n_neighbors):
            par = [
                ('READ_F', 1),
                ('INIT_FILE', base_path + '/verilog/' + parent_name + '_n_c.rom'),
                ('WRITE_F', 1 if i == 0 else 0),
                ('OUTPUT_FILE', base_path + '/verilog/' + parent_name + '_/n_c_out%d.rom' % i)
            ]
            con = [
                ('clk', clk),
                ('rd', Int(1, 1, 10)),
                ('rd_addr0', va[i * node_bits:node_bits * (i + 1)]),
                ('rd_addr1', vb[i * node_bits:node_bits * (i + 1)]),
                ('out0', cva_t[i * cell_bits:cell_bits * (i + 1)]),
                ('out1', cvb_t[i * cell_bits:cell_bits * (i + 1)]),
                ('wr', Int(0, 1, 10)),  # TODO
                ('wr_addr', Int(0, node_bits, 10)),  # TODO
                ('wr_data', Int(0, cell_bits, 10)),  # TODO
            ]
            aux = self.create_memory_2r_1w(cell_bits, node_bits)
            m.Instance(aux, '%s_%d' % (aux.name, i), par, con)
        m.EmbeddedCode('// #####')

        m.EmbeddedCode('')
        m.EmbeddedCode('// line column finder stage lc_table instantiation')
        aux = self.create_lc_table()
        par = []
        con = [
            ('ca', ca),
            ('cb', cb),
            ('lca', lca_t),
            ('lcb', lcb_t),
        ]
        m.Instance(aux, "%s_c" % aux.name, par, con)

        for i in range(n_neighbors):
            par = []
            con = [
                ('ca', cva[i * cell_bits:cell_bits * (i + 1)]),
                ('cb', cvb[i * cell_bits:cell_bits * (i + 1)]),
                ('lca', lcva_t[i * lc_bits:lc_bits * (i + 1)]),
                ('lcb', lcvb_t[i * lc_bits:lc_bits * (i + 1)]),
            ]
            m.Instance(aux, '%s_v_%d' % (aux.name, (i)), par, con)
        m.EmbeddedCode('// #####')

        _u.initialize_regs(m)

        self.cache[name] = m

        return m
