import os
import time

import src.util.per_enum
from src.python.sw.yoto_pipeline.yoto_pipeline_sw import YotoPipelineSw
from src.cython.sw.yoto_pipeline.yoto_pipeline_sw import YotoPipelineSwOpt
from src.python.util.per_graph import PeRGraph
from src.python.util.per_enum import ArchType
from src.python.util.util import Util


def run_connected_graphs():
    threads_per_copy: int = 6
    total_threads: int = 60
    random_seed: int = 0
    arch_type: ArchType = ArchType.ONE_HOP
    arch_type_opt = src.util.per_enum.ArchType.ONE_HOP
    make_shuffle: bool = True
    distance_table_bits: int = 4

    root_path: str = Util.get_project_root()
    dot_path_base = root_path + '/benchmarks/'
    dot_connected_path = dot_path_base + 'connected/'

    output_path_base = os.getcwd() + '/results/sw/yoto/yoto_pipeline/t_%d/%s/' % (total_threads, arch_type)

    output_path = output_path_base

    '''if not os.path.exists(output_path):
        os.makedirs(output_path)'''

    # list connected benchmarks
    dots_list = Util.get_files_list_by_extension(dot_connected_path, '.dot')

    # FIXME the line below is only for debugging
    dots_list = [[dot_connected_path + 'jpeg_idct_ifast.dot', 'jpeg_idct_ifast.dot']]
    for dot_path, dot_name in dots_list:
        per_graph = PeRGraph(dot_path, dot_name)
        print(per_graph.dot_name)

        yoto_pipeline_sw = YotoPipelineSw(per_graph, arch_type, distance_table_bits, make_shuffle, threads_per_copy, )
        start_p = time.time()
        #raw_report: dict = yoto_pipeline_sw.run_single(total_threads // threads_per_copy)
        end_p = time.time()
        print(f'Pure Python execution: {end_p-start_p}sw')

        per_graph_opt = src.cython.util.per_graph.PeRGraph(dot_path, dot_name)
        yoto_pipeline_sw_opt = YotoPipelineSwOpt(per_graph_opt, arch_type_opt, distance_table_bits, make_shuffle, threads_per_copy, )
        start_o = time.time()
        raw_report: dict = yoto_pipeline_sw_opt.run_single(total_threads // threads_per_copy)
        end_o = time.time()
        print(f'Pure Python execution: {end_o - start_o}sw')

        #formatted_report = Util.get_formatted_report(raw_report)
        #Util.save_json(output_path, dot_name, formatted_report)
        #random_seed += 1


if __name__ == '__main__':
    run_connected_graphs()
