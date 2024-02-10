import os
import time
from src.sw.sa_pipeline.sa_pipeline_sw import SAPipeline
from src.util.per_graph import PeRGraph
from src.util.per_enum import ArchType
from src.util.util import get_project_root, get_files_list_by_extension, get_formatted_report, save_json


def run_connected_graphs():
    arch_types = [ArchType.ONE_HOP, ArchType.MESH]
    total_threads = [60, 600]

    threads_per_copy: int = 6
    make_shuffle: bool = True
    distance_table_bits: int = 2

    root_path: str = get_project_root()
    dot_path_base = root_path + '/dot_db/'
    dot_connected_path = dot_path_base + 'connected/'

    # list connected benchmarks
    dots_list = get_files_list_by_extension(dot_connected_path, '.dot')

    # FIXME the line below is only for debugging
    # dots_list = [[dot_connected_path + 'mac.dot', 'mac.dot']]

    for th in total_threads:
        for arch_type in arch_types:
            for dot_path, dot_name in dots_list:
                print(f'TH: {th}, ARCH: {arch_type}, DOT: {dot_name}')
                per_graph = PeRGraph(dot_path, dot_name)
                sa_pipeline = SAPipeline(per_graph, arch_type, distance_table_bits, make_shuffle, threads_per_copy)

                start_time = time.time()
                # raw_report = sa_pipeline.run_single(th // threads_per_copy)
                raw_report = sa_pipeline.run_parallel(th // threads_per_copy)
                end_time = time.time()
                print("Elapsed time: " + str(end_time - start_time))
                print()

                output_path = (
                        get_project_root() + '/reports/sw/sa/sa_pipeline_mp/t_%d/ArchType.%s/' % (th, arch_type))
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                formatted_report = get_formatted_report(raw_report)
                save_json(output_path, formatted_report['graph_name'], formatted_report)


if __name__ == '__main__':
    start_time = time.time()
    run_connected_graphs()
    end_time = time.time()
    print("Total time: " + str(end_time - start_time))
