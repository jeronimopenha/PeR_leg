from veriloggen import *

from src.util.per_enum import ArchType
from src.util.per_graph import PeRGraph
from src.util.piplinebase import PiplineBase
from src.util.util import Util
from src.util.hw_components import HwComponents


class YotoPipelineHw(PiplineBase):
    def __init__(self, per_graph: PeRGraph, arch_type: ArchType, distance_table_bits: int, make_shuffle: bool,
                 n_threads: int = 1):
        self.len_pipeline: int = 6
        super().__init__(per_graph, arch_type, distance_table_bits, make_shuffle, self.len_pipeline, n_threads, )
        self.hw_components = HwComponents()

    def create_stage0_yoto(self) -> Module:
        name = 'stage0_yoto'
        m = Module(name)

        th_bits = Util.get_n_bits(self.n_threads)
        edge_bits = Util.get_n_bits(self.per_graph.n_cells)

        clk = m.Input('clk')
        rst = m.Input('rst')
        start = m.Input('start')
        done = m.OutputReg('done')

        visited_edges = m.Input('visited_edges', edge_bits)

        th_idx = m.OutputReg('th_idx', th_bits)
        th_valid = m.OutputReg('th_valid')
        edg_n = m.OutputReg('edg_n', edge_bits)
        incr_edg = m.OutputReg('incr_edg')
        total_pipeline_counter = m.OutputReg('total_pipeline_counter', 32)
        st5_place = m.Input('st5_place')

        st0_th_idx = m.Wire('st0_th_idx', th_bits)
        st0_th_valid = m.Wire('st0_th_valid')
        st0_edg_n = m.Wire('st0_edg_n', edge_bits)
        st0_incr_edge = m.Wire('st0_incr_edge')

        edge_counter = m.Reg('edge_counter', edge_bits + 1, self.n_threads)
        thread_valid = m.Reg('thread_valid', self.n_threads)
        thread_done = m.Reg('thread_done', self.n_threads)
        next_th_idx = m.Reg('next_th_idx', th_bits + 1)
        running = m.Reg('running')

        m.EmbeddedCode('')
        st0_th_idx.assign(th_idx)
        st0_th_valid.assign(th_valid)
        st0_edg_n.assign(edg_n)
        st0_incr_edge.assign(incr_edg)

        m.Always(Posedge(clk))(
            If(rst)(
                done(Int(0, 1, 10)),
                total_pipeline_counter(Int(0, total_pipeline_counter.width, 10)),

                thread_valid(Int(pow(2, self.n_threads) - 1, thread_valid.width, 2)),
                thread_done(Int(0, thread_done.width, 10)),
                next_th_idx(Int(0, next_th_idx.width, 10)),

                th_idx(Int(0, 1, 10)),
                th_valid(Int(0, 1, 10)),
                edg_n(Int(0, edg_n.width, 10)),
                incr_edg(Int(0, 1, 10)),

                running(Int(0, 1, 10)),
            ).Elif(start)(
                total_pipeline_counter(total_pipeline_counter + Int(1, total_pipeline_counter.width, 10)),

                th_idx(next_th_idx),
                th_valid(thread_valid[next_th_idx]),
                incr_edg(st5_place),

                If(next_th_idx == Int(self.len_pipeline - 1, next_th_idx.width, 10))(
                    next_th_idx(Int(0, next_th_idx.width, 10)),
                    running(Int(1, 1, 10)),
                ).Else(
                    next_th_idx(next_th_idx + Int(1, next_th_idx.width, 10)),
                ),
                If(st0_incr_edge)(
                    edge_counter[st0_th_idx](st0_edg_n),
                ),
                If(AndList(st0_th_valid, st0_incr_edge, st0_edg_n == visited_edges))(
                    thread_valid[st0_th_idx](Int(0, 1, 10)),
                    thread_done[st0_th_idx](Int(1, 1, 10)),
                ),
                If(Uand(thread_done))(
                    done(Int(1, 1, 10))
                ),
                If(~running)(
                    edg_n(Int(0, edg_n.width, 10)),
                ).Else(
                    edg_n(Mux(~st5_place,
                              edge_counter[th_idx],
                              edge_counter[th_idx] + Int(1, edg_n.width)
                              )),
                )
            )
        )
        return m

    def create_stage1_yoto(self, init_file: str) -> Module:
        name = 'stage1_yoto'
        m = Module(name)

        th_bits = Util.get_n_bits(self.n_threads)
        edge_bits = Util.get_n_bits(self.per_graph.n_cells)
        dst_tbl_bits = self.distance_table_bits
        node_bits = Util.get_n_bits(self.per_graph.n_cells)

        clk = m.Input('clk')
        rst = m.Input('rst')

        th_idx = m.OutputReg('th_idx', th_bits)
        th_valid = m.OutputReg('th_valid')
        dist_table_line = m.OutputReg('dist_table_line', dst_tbl_bits)
        a = m.OutputReg('a', node_bits)
        b = m.OutputReg('b', node_bits)

        st0_th_idx = m.Input('st0_th_idx', th_bits)
        st0_th_valid = m.Input('st0_th_valid')
        st0_edg_n = m.Input('st0_edg_n', edge_bits)

        a_t = m.Wire('a_t', node_bits)
        b_t = m.Wire('b_t', node_bits)

        m.Always(Posedge(clk))(
            If(rst)(
                th_idx(Int(0, th_idx.width, 10)),
                th_valid(Int(0, th_valid.width, 10)),
                dist_table_line(Int(0, dist_table_line.width, 10)),
                a(Int(0, a.width, 10)),
                b(Int(0, b.width, 10)),
            ).Else(
                th_idx(st0_th_idx),
                th_valid(st0_th_valid),
                a(a_t),
                b(b_t),
                dist_table_line(Xor(Cat(Int(0, dst_tbl_bits - th_bits, 10), st0_th_idx), st0_edg_n[0:dst_tbl_bits])),
            )
        )
        par = [
            ('width', node_bits * 2),
            ('depth', th_bits + edge_bits),
            ('read_f', 1),
            ('init_file', init_file),
            ('write_f', 0),
            ('output_file', 'mem_out_file.txt'),
        ]
        con = [
            ('rd_addr', Cat(st0_th_idx, st0_edg_n)),
            ('out', Cat(a_t, b_t)),
            ('wr', Int(0, 1, 10)),
            ('wr_addr', Int(0, edge_bits + th_bits, 10)),
            ('wr_data', Int(0, node_bits * 2, 10)),
        ]

        edges_m = self.hw_components.create_memory_1r_1w()
        m.Instance(edges_m, edges_m.name, par, con)

        return m

    def create_stage2_yoto(self, init_file: str, mem_out_file: str) -> Module:
        name = 'stage2_yoto'
        m = Module(name)

        th_bits = Util.get_n_bits(self.n_threads)
        dst_tbl_bits = self.distance_table_bits
        node_bits = Util.get_n_bits(self.per_graph.n_cells)
        ij_bits = Util.get_n_bits(self.n_lines)

        clk = m.Input('clk')
        rst = m.Input('rst')

        th_idx = m.OutputReg('th_idx', th_bits)
        th_valid = m.OutputReg('th_valid')
        ia = m.OutputReg('ia', ij_bits)
        ja = m.OutputReg('ja', ij_bits)
        dist_table_line = m.OutputReg('dist_table_line', dst_tbl_bits)
        dist_counter = m.OutputReg('dist_counter', 6)
        b = m.OutputReg('b', node_bits)

        st1_th_idx = m.Input('st1_th_idx', th_bits)
        st1_th_valid = m.Input('st1_th_valid')
        st1_dist_table_line = m.Input('st1_dist_table_line', dst_tbl_bits)
        st1_a = m.Input('st1_a', node_bits)
        st1_b = m.Input('st1_b', node_bits)

        st4_th_idx = m.Input('st4_th_idx', th_bits)
        st4_th_valid = m.Input('st4_th_valid')
        st4_place = m.Input('st4_place')
        st4_dist_counter = m.Input('st4_dist_counter', 6)
        st4_ib = m.Input('st4_ib', ij_bits)
        st4_jb = m.Input('st4_jb', ij_bits)
        st4_b = m.Input('st4_b', node_bits)

        th_dist_table_counter = m.Reg('th_dist_table_counter', 6, self.n_threads)
        running = m.Reg('running')
        ia_t = m.Wire('ia_t', ij_bits)
        ja_t = m.Wire('ja_t', ij_bits)

        m.Always(Posedge(clk))(
            If(rst)(
                th_idx(Int(0, th_idx.width, 10)),
                th_valid(Int(0, 1, 10)),
                ia(Int(0, ia.width, 10)),
                ja(Int(0, ja.width, 10)),
                dist_table_line(Int(0, dist_table_line.width, 10)),
                dist_counter(Int(0, dist_counter.width, 10)),
                b(Int(0, b.width, 10)),
                running(Int(0, 1, 10))
            ).Else(
                th_idx(st1_th_idx),
                th_valid(st1_th_valid),
                ia(ia_t),
                ja(ja_t),
                dist_table_line(st1_dist_table_line),
                b(st1_b),
                If(st4_place)(
                    th_dist_table_counter[st4_th_idx](Int(0, th_dist_table_counter.width, 10))
                ).Elif(st4_th_valid)(
                    th_dist_table_counter[st4_th_idx](st4_dist_counter + Int(1, th_dist_table_counter.width, 10))
                ),
                If(~running)(
                    dist_counter(Int(0, dist_counter.width, 10))
                ).Else(
                    dist_counter(th_dist_table_counter[st1_th_idx])
                ),
                If(st1_th_idx == Int(self.len_pipeline - 1, st1_th_idx.width, 10))(
                    running(Int(1, 1, 10)),
                ),
            )
        )

        par = [
            ('width', ij_bits * 2),
            ('depth', th_bits + node_bits),
            ('read_f', 1),
            ('init_file', init_file),
            ('write_f', 1),
            ('output_file', mem_out_file),
        ]
        con = [
            ('rd_addr', Cat(st1_th_idx, st1_a)),
            ('out', Cat(ia_t, ja_t)),
            ('wr', st4_place),
            ('wr_addr', Cat(st4_th_idx, st4_b)),
            ('wr_data', Cat(st4_ib, st4_jb)),
        ]

        n2c_m = self.hw_components.create_memory_1r_1w()
        m.Instance(n2c_m, n2c_m.name, par, con)

        return m


threads_per_copy: int = 6
total_threads: int = 6
arch_type: ArchType = ArchType.ONE_HOP
make_shuffle: bool = True
distance_table_bits: int = 4

root_path: str = Util.get_project_root()
dot_path_base = root_path + '/dot_db/'
dot_connected_path = dot_path_base + 'connected/'

dots_list = [dot_connected_path + 'mac.dot', 'mac.dot']
per_graph = PeRGraph(dots_list[0], dots_list[1])
yoto_pipeline_hw = YotoPipelineHw(per_graph, arch_type, distance_table_bits, make_shuffle, threads_per_copy)
yoto_pipeline_hw.create_stage2_yoto('test.rom', 'test.rom').to_verilog('teste.v')
