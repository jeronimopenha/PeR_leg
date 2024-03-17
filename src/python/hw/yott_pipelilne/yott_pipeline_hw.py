from veriloggen import *
from src.python.util.hw_components import HwComponents
from src.python.util.per_enum import ArchType
from src.python.util.per_graph import PeRGraph
from src.python.util.piplinebase import PiplineBase
from src.python.util.util import Util


class YottPipelineHw(PiplineBase):
    def __init__(self, per_graph: PeRGraph, arch_type: ArchType, distance_table_bits: int, make_shuffle: bool,
                 n_threads: int = 10):
        self.len_pipeline: int = 6
        super().__init__(per_graph, arch_type, distance_table_bits, make_shuffle, self.len_pipeline, n_threads, )
        self.hw_components = HwComponents()
        self.th_bits = Util.get_n_bits(self.n_threads)
        self.edge_bits = Util.get_n_bits(self.per_graph.n_cells)
        self.node_bits = Util.get_n_bits(self.per_graph.n_cells)
        self.ij_bits = Util.get_n_bits(self.n_lines)
        self.total_dists = pow((self.n_lines * 2) - 1, 2)
        self.dst_counter_bits = 6
        self.fifo_width = self.th_bits + 1
        self.fifo_depth_bits = self.th_bits + 1
        # fixme uncomment the line below and comment the line above
        # self.dst_counter_bits = Util.get_n_bits(self.total_dists) + 1

    def create_yott_pipeline_hw(self) -> Module:
        name = "yoto_pipeline_hw"
        m = Module(name)

        clk = m.Input('clk')
        rst = m.Input('rst')
        start = m.Input('start')
        visited_edges = m.Input('visited_edges', self.edge_bits)
        done = m.Output('done')

        '''st1_conf_wr = m.Input('st1_conf_wr')
        st1_conf_addr = m.Input('st1_conf_addr', self.edge_bits + self.th_bits)
        st1_conf_data = m.Input('st1_conf_data', self.node_bits * 2)
        st2_wr_conf_addr = m.Input('st2_wr_conf_addr', self.th_bits + self.node_bits)
        st2_rd_conf_addr = m.Input('st2_rd_conf_addr', self.th_bits + self.node_bits)
        st2_conf_wr = m.Input('st2_conf_wr')
        st2_conf_wr_data = m.Input('st2_conf_wr_data', self.ij_bits * 2)
        st2_conf_rd = m.Input('st2_conf_rd')
        st2_conf_rd_data = m.Output('st2_conf_rd_data', self.ij_bits * 2)
        st3_conf_wr = m.Input('st3_conf_wr')
        st3_conf_addr = m.Input('st3_conf_addr', self.dst_counter_bits - 1 + self.distance_table_bits)
        st3_conf_data = m.Input('st3_conf_data', (self.ij_bits + 1) * 2)
        st4_conf_wr = m.Input('st4_conf_wr')
        st4_conf_addr = m.Input('st4_conf_addr', self.th_bits + self.ij_bits * 2)
        st4_conf_data = m.Input('st4_conf_data')'''

        m.EmbeddedCode('// St0 wires')
        st0_th_idx = m.Wire('st0_th_idx', self.th_bits)
        st0_th_valid = m.Wire('st0_th_valid')
        st0_edg_n = m.Wire('st0_edg_n', self.edge_bits)
        st0_incr_edg = m.Wire('st0_incr_edg')
        m.EmbeddedCode('// -----')
        m.EmbeddedCode('')

        m.EmbeddedCode('// St1 wires')
        st1_thread_index = m.Wire('st1_thread_index')
        st1_thread_valid = m.Wire('st1_thread_valid')
        st1_should_write = m.Wire('st1_should_write')
        st1_fifo_write_enable = m.Wire('st1_fifo_write_enable')
        st1_fifo_input_data = m.Wire('st1_fifo_input_data', self.fifo_width)
        m.EmbeddedCode('// -----')
        m.EmbeddedCode('')

        m.EmbeddedCode('// St2 wires')

        m.EmbeddedCode('// -----')
        m.EmbeddedCode('')

        m.EmbeddedCode('// St3 wires')

        m.EmbeddedCode('// -----')
        m.EmbeddedCode('')

        m.EmbeddedCode('// St4 wires')

        m.EmbeddedCode('// -----')
        m.EmbeddedCode('')

        m.EmbeddedCode('// St5 wires')

        m.EmbeddedCode('// -----')
        m.EmbeddedCode('')

        m.EmbeddedCode('// St6 wires')

        m.EmbeddedCode('// -----')
        m.EmbeddedCode('')

        m.EmbeddedCode('// St7 wires')

        m.EmbeddedCode('// -----')
        m.EmbeddedCode('')

        m.EmbeddedCode('// St8 wires')

        m.EmbeddedCode('// -----')
        m.EmbeddedCode('')

        m.EmbeddedCode('// St9 wires')

        m.EmbeddedCode('// -----')
        m.EmbeddedCode('')

        m.EmbeddedCode('// St10 wires')

        m.EmbeddedCode('// -----')
        m.EmbeddedCode('')

        m.EmbeddedCode('// St0 instantiation')
        stage0_m = self.create_stage0_yott()
        par = []
        con = [
            ('clk', clk),
            ('rst', rst),
            ('start', start),
            ('thread_index', st1_thread_index),
            ('thread_valid', st1_thread_valid),
            ('should_write', st1_should_write),
            ('fifo_write_enable', st1_fifo_write_enable),
            ('fifo_input_data', st1_fifo_input_data),
        ]
        m.Instance(stage0_m, stage0_m.name, par, con)
        m.EmbeddedCode('// -----')

        m.EmbeddedCode('// St1 instantiation')
        '''stage1_m = self.create_stage1_yoto(edges_rom_f, simulate)
        con = [
            ('clk', clk),
            ('rst', rst),
            ('visited_edges', visited_edges),
            ('th_idx', st1_th_idx),
            ('th_valid', st1_th_valid),
            ('dist_table_line', st1_dist_table_line),
            ('a', st1_a),
            ('b', st1_b),
            ('st0_th_idx', st0_th_idx),
            ('st0_th_valid', st0_th_valid),
            ('st0_edg_n', st0_edg_n),
            ('conf_wr', st1_conf_wr),
            ('conf_addr', st1_conf_addr),
            ('conf_data', st1_conf_data),
        ]
        m.Instance(stage1_m, stage1_m.name, par, con)'''
        m.EmbeddedCode('// -----')

        m.EmbeddedCode('// St2 instantiation')
        '''stage2_m = self.create_stage2_yoto(n2c_rom_f, n2c_out_f, simulate)
        con = [
            ('clk', clk),
            ('rst', rst),
            ('th_idx', st2_th_idx),
            ('th_valid', st2_th_valid),
            ('ia', st2_ia),
            ('ja', st2_ja),
            ('dist_table_line', st2_dist_table_line),
            ('dist_counter', st2_dist_counter),
            ('b', st2_b),
            ('st1_th_idx', st1_th_idx),
            ('st1_th_valid', st1_th_valid),
            ('st1_dist_table_line', st1_dist_table_line),
            ('st1_a', st1_a),
            ('st1_b', st1_b),
            ('st4_th_idx', st4_th_idx),
            ('st4_th_valid', st4_th_valid),
            ('st4_place', st4_place),
            ('st4_dist_counter', st4_dist_counter),
            ('st4_ib', st4_ib),
            ('st4_jb', st4_jb),
            ('st4_b', st4_b),
            ('conf_wr_addr', st2_wr_conf_addr),
            ('conf_rd_addr', st2_rd_conf_addr),
            ('conf_wr', st2_conf_wr),
            ('conf_wr_data', st2_conf_wr_data),
            ('conf_rd', st2_conf_rd),
            ('conf_rd_data', st2_conf_rd_data),
        ]
        m.Instance(stage2_m, stage2_m.name, par, con)'''
        m.EmbeddedCode('// -----')

        m.EmbeddedCode('// St3 instantiation')
        '''stage3_m = self.create_stage3_yoto(dst_tbl_rom_f, simulate)
        con = [
            ('clk', clk),
            ('rst', rst),
            ('th_idx', st3_th_idx),
            ('th_valid', st3_th_valid),
            ('ib', st3_ib),
            ('jb', st3_jb),
            ('dist_counter', st3_dist_counter),
            ('b', st3_b),
            ('st2_th_idx', st2_th_idx),
            ('st2_th_valid', st2_th_valid),
            ('st2_ia', st2_ia),
            ('st2_ja', st2_ja),
            ('st2_dist_table_line', st2_dist_table_line),
            ('st2_dist_counter', st2_dist_counter),
            ('st2_b', st2_b),
            ('conf_wr', st3_conf_wr),
            ('conf_addr', st3_conf_addr),
            ('conf_data', st3_conf_data),
        ]
        m.Instance(stage3_m, stage3_m.name, par, con)'''
        m.EmbeddedCode('// -----')

        m.EmbeddedCode('// St4 instantiation')
        '''stage4_m = self.create_stage4_yoto(cell_content_f, simulate)
        con = [
            ('clk', clk),
            ('rst', rst),
            ('th_idx', st4_th_idx),
            ('th_valid', st4_th_valid),
            ('place', st4_place),
            ('ib', st4_ib),
            ('jb', st4_jb),
            ('dist_counter', st4_dist_counter),
            ('b', st4_b),
            ('st3_th_idx', st3_th_idx),
            ('st3_th_valid', st3_th_valid),
            ('st3_ib', st3_ib),
            ('st3_jb', st3_jb),
            ('st3_dist_counter', st3_dist_counter),
            ('st3_b', st3_b),
            ('conf_wr', st4_conf_wr),
            ('conf_addr', st4_conf_addr),
            ('conf_data', st4_conf_data),
        ]
        m.Instance(stage4_m, stage4_m.name, par, con)'''
        m.EmbeddedCode('// -----')

        m.EmbeddedCode('// St5 instantiation')
        '''stage4_m = self.create_stage4_yoto(cell_content_f, simulate)
        con = [
            ('clk', clk),
            ('rst', rst),
            ('th_idx', st4_th_idx),
            ('th_valid', st4_th_valid),
            ('place', st4_place),
            ('ib', st4_ib),
            ('jb', st4_jb),
            ('dist_counter', st4_dist_counter),
            ('b', st4_b),
            ('st3_th_idx', st3_th_idx),
            ('st3_th_valid', st3_th_valid),
            ('st3_ib', st3_ib),
            ('st3_jb', st3_jb),
            ('st3_dist_counter', st3_dist_counter),
            ('st3_b', st3_b),
            ('conf_wr', st4_conf_wr),
            ('conf_addr', st4_conf_addr),
            ('conf_data', st4_conf_data),
        ]
        m.Instance(stage4_m, stage4_m.name, par, con)'''
        m.EmbeddedCode('// -----')

        m.EmbeddedCode('// St6 instantiation')
        '''stage4_m = self.create_stage4_yoto(cell_content_f, simulate)
        con = [
            ('clk', clk),
            ('rst', rst),
            ('th_idx', st4_th_idx),
            ('th_valid', st4_th_valid),
            ('place', st4_place),
            ('ib', st4_ib),
            ('jb', st4_jb),
            ('dist_counter', st4_dist_counter),
            ('b', st4_b),
            ('st3_th_idx', st3_th_idx),
            ('st3_th_valid', st3_th_valid),
            ('st3_ib', st3_ib),
            ('st3_jb', st3_jb),
            ('st3_dist_counter', st3_dist_counter),
            ('st3_b', st3_b),
            ('conf_wr', st4_conf_wr),
            ('conf_addr', st4_conf_addr),
            ('conf_data', st4_conf_data),
        ]
        m.Instance(stage4_m, stage4_m.name, par, con)'''
        m.EmbeddedCode('// -----')

        m.EmbeddedCode('// St7 instantiation')
        '''stage4_m = self.create_stage4_yoto(cell_content_f, simulate)
        con = [
            ('clk', clk),
            ('rst', rst),
            ('th_idx', st4_th_idx),
            ('th_valid', st4_th_valid),
            ('place', st4_place),
            ('ib', st4_ib),
            ('jb', st4_jb),
            ('dist_counter', st4_dist_counter),
            ('b', st4_b),
            ('st3_th_idx', st3_th_idx),
            ('st3_th_valid', st3_th_valid),
            ('st3_ib', st3_ib),
            ('st3_jb', st3_jb),
            ('st3_dist_counter', st3_dist_counter),
            ('st3_b', st3_b),
            ('conf_wr', st4_conf_wr),
            ('conf_addr', st4_conf_addr),
            ('conf_data', st4_conf_data),
        ]
        m.Instance(stage4_m, stage4_m.name, par, con)'''
        m.EmbeddedCode('// -----')

        m.EmbeddedCode('// St8 instantiation')
        '''stage4_m = self.create_stage4_yoto(cell_content_f, simulate)
        con = [
            ('clk', clk),
            ('rst', rst),
            ('th_idx', st4_th_idx),
            ('th_valid', st4_th_valid),
            ('place', st4_place),
            ('ib', st4_ib),
            ('jb', st4_jb),
            ('dist_counter', st4_dist_counter),
            ('b', st4_b),
            ('st3_th_idx', st3_th_idx),
            ('st3_th_valid', st3_th_valid),
            ('st3_ib', st3_ib),
            ('st3_jb', st3_jb),
            ('st3_dist_counter', st3_dist_counter),
            ('st3_b', st3_b),
            ('conf_wr', st4_conf_wr),
            ('conf_addr', st4_conf_addr),
            ('conf_data', st4_conf_data),
        ]
        m.Instance(stage4_m, stage4_m.name, par, con)'''
        m.EmbeddedCode('// -----')

        m.EmbeddedCode('// St9 instantiation')
        '''stage4_m = self.create_stage4_yoto(cell_content_f, simulate)
        con = [
            ('clk', clk),
            ('rst', rst),
            ('th_idx', st4_th_idx),
            ('th_valid', st4_th_valid),
            ('place', st4_place),
            ('ib', st4_ib),
            ('jb', st4_jb),
            ('dist_counter', st4_dist_counter),
            ('b', st4_b),
            ('st3_th_idx', st3_th_idx),
            ('st3_th_valid', st3_th_valid),
            ('st3_ib', st3_ib),
            ('st3_jb', st3_jb),
            ('st3_dist_counter', st3_dist_counter),
            ('st3_b', st3_b),
            ('conf_wr', st4_conf_wr),
            ('conf_addr', st4_conf_addr),
            ('conf_data', st4_conf_data),
        ]
        m.Instance(stage4_m, stage4_m.name, par, con)'''
        m.EmbeddedCode('// -----')

        m.EmbeddedCode('// St10 instantiation')
        '''stage4_m = self.create_stage4_yoto(cell_content_f, simulate)
        con = [
            ('clk', clk),
            ('rst', rst),
            ('th_idx', st4_th_idx),
            ('th_valid', st4_th_valid),
            ('place', st4_place),
            ('ib', st4_ib),
            ('jb', st4_jb),
            ('dist_counter', st4_dist_counter),
            ('b', st4_b),
            ('st3_th_idx', st3_th_idx),
            ('st3_th_valid', st3_th_valid),
            ('st3_ib', st3_ib),
            ('st3_jb', st3_jb),
            ('st3_dist_counter', st3_dist_counter),
            ('st3_b', st3_b),
            ('conf_wr', st4_conf_wr),
            ('conf_addr', st4_conf_addr),
            ('conf_data', st4_conf_data),
        ]
        m.Instance(stage4_m, stage4_m.name, par, con)'''
        m.EmbeddedCode('// -----')

        return m

    def create_stage0_yott(self) -> Module:
        name = 'stage0_yott'
        m = Module(name)

        clk = m.Input('clk')
        rst = m.Input('rst')
        start = m.Input('start')

        thread_index = m.Output('thread_index')
        thread_valid = m.Output('thread_valid')
        should_write = m.Output('should_write')

        fifo_write_enable = m.Input('fifo_write_enable')
        fifo_input_data = m.Input('fifo_input_data', self.fifo_width)

        fifo_output_read_enable = m.Reg('fifo_output_read_enable')
        fifo_output_valid = m.Wire('fifo_output_valid')
        fifo_output_data = m.Wire('fifo_output_data', self.fifo_width)
        fifo_empty = m.Wire('fifo_empty')
        fifo_almostempty = m.Wire('fifo_almostempty')
        fifo_full = m.Wire('fifo_full')
        fifo_almostfull = m.Wire('fifo_almostfull')
        fifo_data_count = m.Wire('fifo_data_count', self.fifo_depth_bits + 1)

        flag_wait = m.Reg('flag_wait')

        m.EmbeddedCode('')
        thread_index.assign(fifo_output_data[1:self.fifo_width])
        thread_valid.assign(fifo_output_valid)
        should_write.assign(fifo_output_data[0])

        m.Always(Posedge(clk))(
            If(rst)(
                fifo_output_read_enable(Int(0, 1, 2)),
                flag_wait(Int(0, 1, 2)),
            ).Elif(start)(
                fifo_output_read_enable(Int(0, 1, 2)),
                If(fifo_almostempty)(
                    If(~flag_wait)(
                        fifo_output_read_enable(Int(1, 1, 2)),
                    ),
                    flag_wait(~flag_wait)
                ).Elif(~fifo_empty)(
                    fifo_output_read_enable(Int(1, 1, 2))
                )
            )
        )

        par = [
            ('FIFO_WIDTH', self.fifo_width),
            ('FIFO_DEPTH_BITS', self.fifo_depth_bits),
            ('FIFO_ALMOSTFULL_THRESHOLD', Power(2, self.fifo_depth_bits) - 4),
            ('FIFO_ALMOSTEMPTY_THRESHOLD', 4),
        ]

        con = [
            ('clk', clk),
            ('rst', rst),
            ('write_enable', fifo_write_enable),
            ('input_data', fifo_input_data),
            ('output_read_enable', fifo_write_enable),
            ('output_valid', fifo_output_valid),
            ('output_data', fifo_output_data),
            ('empty', fifo_empty),
            ('almostempty', fifo_almostempty),
            ('full', fifo_full),
            ('almostfull', fifo_almostfull),
            ('data_count', fifo_data_count),
        ]
        fifo = self.hw_components.create_fifo()
        m.Instance(fifo, fifo.name, par, con)
        return m
