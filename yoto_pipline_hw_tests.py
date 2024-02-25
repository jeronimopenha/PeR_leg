import os
import random

from src.python.hw.yoto_pipeline.yoto_pipeline_hw import YotoPipelineHw
from src.python.util.per_graph import PeRGraph
from src.python.util.per_enum import ArchType
from src.python.util.util import Util


def run_connected_graphs():
    # fixme
    random.seed(0)
    threads_per_copy: int = 6
    total_threads: int = 6
    arch_type: ArchType = ArchType.ONE_HOP
    make_shuffle: bool = True
    distance_table_bits: int = 4
    simul = True

    root_path: str = Util.get_project_root()
    dot_path_base = root_path + '/dot_db/'
    dot_connected_path = dot_path_base + 'connected/'

    report_path_base = os.getcwd() + '/reports/sw/yoto/yoto_pipeline/t_%d/%s/' % (total_threads, arch_type)
    verilog_path_base = os.getcwd() + '/verilog/yoto/yoto_pipeline/t_%d/%s/' % (total_threads, arch_type)

    Util.create_folder_if_not_exist(report_path_base)
    Util.create_folder_if_not_exist(verilog_path_base)

    # list connected benchmarks
    # dots_list = Util.get_files_list_by_extension(dot_connected_path, '.dot')

    # FIXME the line below is only for debugging
    dots_list = [[dot_connected_path + 'mac.dot', 'mac.dot']]
    for dot_path, dot_name in dots_list:
        per_graph = PeRGraph(dot_path, dot_name)
        print(per_graph.dot_name)
        yoto_pipeline_hw = YotoPipelineHw(per_graph, arch_type, distance_table_bits, make_shuffle, threads_per_copy, )
        yoto_pipeline_hw.create_yoto_pipeline_hw_test_bench(verilog_path_base, True)
        '''raw_report: dict = yoto_pipeline_hw.run(total_threads // threads_per_copy)
        formatted_report = Util.get_formatted_report(raw_report)
        Util.save_json(output_path, dot_name, formatted_report)'''


if __name__ == '__main__':
    run_connected_graphs()
