import os
from src.sw.yoto_pipeline.yoto_pipeline_sw import YotoPipelineSw
from src.util.per_graph import PeRGraph
from src.util.per_enum import ArchType
from src.util.util import Util


def run_connected_graphs():
    threads_per_copy: int = 6
    total_threads: int = 6
    random_seed: int = 0
    arch_type: ArchType = ArchType.ONE_HOP
    make_shuffle: bool = True
    distance_table_bits: int = 4

    root_path: str = Util.get_project_root()
    dot_path_base = root_path + '/dot_db/'
    dot_connected_path = dot_path_base + 'connected/'

    output_path_base = os.getcwd() + '/results/sw/yoto/yoto_pipeline/t_%d/%s/' % (total_threads, arch_type)

    output_path = output_path_base

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # list connected benchmarks
    dots_list = Util.get_files_list_by_extension(dot_connected_path, '.dot')

    # FIXME the line below is only for debugging
    # dots_list = [[dot_connected_path + 'arf.dot', 'arf.dot']]
    for dot_path, dot_name in dots_list:
        per_graph = PeRGraph(dot_path, dot_name)
        print(per_graph.dot_name)
        yoto_pipeline_sw = YotoPipelineSw(per_graph, arch_type, distance_table_bits, make_shuffle, threads_per_copy, )
        raw_report: dict = yoto_pipeline_sw.run_parallel(total_threads // threads_per_copy)
        formatted_report = Util.get_formatted_report(raw_report)
        Util.save_json(output_path, dot_name, formatted_report)
        random_seed += 1


if __name__ == '__main__':
    run_connected_graphs()
