from veriloggen import *

from src.util.per_enum import ArchType
from src.util.per_graph import PeRGraph
from src.util.piplinebase import PiplineBase
from src.util.util import Util


class YotoPipelineHw(PiplineBase):
    def __init__(self, per_graph: PeRGraph, arch_type: ArchType, distance_table_bits: int, make_shuffle: bool,
                 n_threads: int = 1):
        self.len_pipeline: int = 6
        super().__init__(per_graph, arch_type, distance_table_bits, make_shuffle, self.len_pipeline, n_threads, )

    def create_stage0_yoto(self, n_edges: int):
        name = 'stage0_yoto'
        m = Module(name)

        clk = m.Input('clk')
        rst = m.Input('rst')
        start = m.Input('start')

        th_idx = m.OutputReg('th_idx', Util.get_n_bits(self.n_threads))
        th_valid = m.OutputReg('th_valid')
        edg_n = m.OutputReg('edg_n', Util.get_n_bits(n_edges))
        incr_edg = m.OutputReg('incr_edg')
        total_pipeline_counter = m.OutputReg('total_pipeline_counter', 32)

        # memory
        '''self.edge_counter = self.Reg('edge_counter', Util.get_n_bits(n_edges))
        self.thread_valid: list[bool] = [True if i < self.n_threads else False for i in range(self.len_pipeline)]
        self.thread_done: list[bool] = [False if i < self.n_threads else True for i in range(self.len_pipeline)]
        self.th_idx: int = 0
        self.done: bool = False'''

        not_first_run = m.Reg('not_first_run')

        m.Always(Posedge(clk))(
            If(rst)(
                th_idx(Int(0, 1, 10)),
                not_first_run(Int(0, 1, 10)),
            ).Elif(start)(
                If(~not_first_run)(

                ).Else(

                )
            )
        )
