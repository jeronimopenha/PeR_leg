import os
import random

from src.old.python.hw import YottPipelineHw
from src.old.python.util.per_graph import PeRGraph
from src.old.python.util.per_enum import ArchType
from src.old.python import Util


def run_connected_graphs():
    # fixme
    random.seed(0)
    threads_per_copy: int = 10
    total_threads: int = 10
    arch_type: ArchType = ArchType.ONE_HOP
    make_shuffle: bool = True
    distance_table_bits: int = 4
    simul = True

    root_path: str = Util.get_project_root()
    dot_path_base = root_path + '/benchmarks/'
    dot_connected_path = dot_path_base + 'connected/'

    report_path_base = os.getcwd() + '/reports/sw/yott/yott_pipeline/t_%d/%s/' % (total_threads, arch_type)
    verilog_path_base = os.getcwd() + '/verilog/yott/yott_pipeline/t_%d/%s/' % (total_threads, arch_type)

    Util.create_folder_if_not_exist(report_path_base)
    Util.create_folder_if_not_exist(verilog_path_base)

    # list connected benchmarks
    # dots_list = Util.get_files_list_by_extension(dot_connected_path, '.dot')

    # FIXME the line below is only for debugging
    dots_list = [[dot_connected_path + 'mac.dot', 'mac.dot']]
    for dot_path, dot_name in dots_list:
        per_graph = PeRGraph(dot_path, dot_name)
        print(per_graph.dot_name)
        yott_pipeline_hw = YottPipelineHw(per_graph, arch_type, distance_table_bits, make_shuffle, threads_per_copy, )
        yott_pipeline_hw.create_yott_pipeline_hw_test_bench(verilog_path_base, True)
        # yott_pipeline_hw.create_manhattan_dist_table().to_verilog('synth.v')
        # yott_pipeline_hw.create_yott_pipeline_hw('','', '', '', '', '', False).to_verilog('synth.v')
        # yott_pipeline_hw.create_yott_pipeline_hw_test_bench(verilog_path_base, True)
        '''raw_report: dict = yott_pipeline_hw.run(total_threads // threads_per_copy)
        formatted_report = Util.get_formatted_report(raw_report)
        Util.save_json(output_path, dot_name, formatted_report)'''


if __name__ == '__main__':
    run_connected_graphs()
