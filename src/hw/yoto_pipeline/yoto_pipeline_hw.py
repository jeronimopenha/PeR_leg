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

        st1_th_idx = m.Wire('st1_th_idx', th_bits)
        st1_th_valid = m.Wire('st1_th_valid')
        st1_edg_n = m.Wire('st1_edg_n', edge_bits)
        st1_incr_edge = m.Wire('st1_incr_edge')

        edge_counter = m.Reg('edge_counter', edge_bits + 1, self.n_threads)
        thread_valid = m.Reg('thread_valid', self.n_threads)
        thread_done = m.Reg('thread_done', self.n_threads)
        next_th_idx = m.Reg('next_th_idx', th_bits + 1)
        runnning = m.Reg('runnning')

        m.EmbeddedCode('')
        st1_th_idx.assign(th_idx)
        st1_th_valid.assign(th_valid)
        st1_edg_n.assign(edg_n)
        st1_incr_edge.assign(incr_edg)

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

                runnning(Int(0, 1, 10)),
            ).Elif(start)(
                total_pipeline_counter(total_pipeline_counter + Int(1, total_pipeline_counter.width, 10)),

                th_idx(next_th_idx),
                th_valid(thread_valid[next_th_idx]),
                incr_edg(st5_place),

                If(next_th_idx == Int(self.len_pipeline - 1, next_th_idx.width, 10))(
                    next_th_idx(Int(0, next_th_idx.width, 10)),
                    runnning(1),
                ).Else(
                    next_th_idx(next_th_idx + Int(1, next_th_idx.width, 10)),
                ),
                If(st1_incr_edge)(
                    edge_counter[st1_th_idx](st1_edg_n),
                ),
                If(AndList(st1_th_valid, st1_incr_edge, st1_edg_n == visited_edges))(
                    thread_valid[st1_th_idx](Int(0, 1, 10)),
                    thread_done[st1_th_idx](Int(1, 1, 10)),
                ),
                If(Uand(thread_done))(
                    done(Int(1, 1, 10))
                ),
                If(~runnning)(
                    edg_n(Mux(~st5_place,
                              Int(0, edg_n.width),
                              Int(1, edg_n.width)
                              )),
                ).Else(
                    edg_n(Mux(~st5_place,
                              edge_counter[th_idx],
                              edge_counter[th_idx] + Int(1, edg_n.width)
                              )),
                )
            )
        )
        return m

    def create_stage1_yoto(self) -> Module:
        name = 'stage1_yoto'
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

        st1_th_idx = m.Wire('st1_th_idx', th_bits)
        st1_th_valid = m.Wire('st1_th_valid')
        st1_edg_n = m.Wire('st1_edg_n', edge_bits)
        st1_incr_edge = m.Wire('st1_incr_edge')

        edge_counter = m.Reg('edge_counter', edge_bits + 1, self.n_threads)
        thread_valid = m.Reg('thread_valid', self.n_threads)
        thread_done = m.Reg('thread_done', self.n_threads)
        next_th_idx = m.Reg('next_th_idx', th_bits + 1)
        runnning = m.Reg('runnning')

        m.EmbeddedCode('')
        st1_th_idx.assign(th_idx)
        st1_th_valid.assign(th_valid)
        st1_edg_n.assign(edg_n)
        st1_incr_edge.assign(incr_edg)

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
yoto_pipeline_hw.create_stage0_yoto().to_verilog('teste.v')
