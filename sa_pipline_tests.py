import os
import multiprocessing as mp
import time
from src.sw.sa_pipeline.sa_pipeline_sw import SAPipeline
from src.util.per_graph import PeRGraph
from src.util.per_enum import ArchType
from src.util.util import Util


def run_connected_graphs():
    arch_types = [ArchType.ONE_HOP, ArchType.MESH]
    total_threads = [6, 60, 600]

    threads_per_copy: int = 6
    make_shuffle: bool = True
    distance_table_bits: int = 2

    root_path: str = Util.get_project_root()
    dot_path_base = root_path + '/dot_db/'
    dot_connected_path = dot_path_base + 'connected/'

    # list connected benchmarks
    dots_list = Util.get_files_list_by_extension(dot_connected_path, '.dot')

    # FIXME the line below is only for debugging
    # dots_list = [[dot_connected_path + 'mac.dot', 'mac.dot']]

    jobs_alive = []
    manager = mp.Manager()
    return_dict = manager.dict()
    for th in total_threads:
        for arch_type in arch_types:
            task_counter = 0
            for dot_path, dot_name in dots_list:
                per_graph = PeRGraph(dot_path, dot_name)
                sa_pipeline = SAPipeline(per_graph, arch_type, distance_table_bits, make_shuffle, threads_per_copy)
                p = mp.Process(target=sa_pipeline.run,
                               args=(str(task_counter), return_dict, th // threads_per_copy,))
                task_counter += 1
                jobs_alive.append(p)
                p.start()
                print(len(jobs_alive))
            while len(jobs_alive) > 0:
                jobs_alive = [job for job in jobs_alive if job.is_alive()]
                time.sleep(1)
            print(len(jobs_alive))
            print(return_dict)
            for j_name in return_dict.keys():
                print(j_name)
                for report in return_dict[j_name]:
                    output_path = (Util.get_project_root() +
                                   '/reports/sw/sa/sa_pipeline/t_%d/ArchType.%s/' %
                                   (report['total_threads'], report['arch_type'])
                                   )

                    if not os.path.exists(output_path):
                        os.makedirs(output_path)
                    raw_report: dict = report
                    formatted_report = Util.get_formatted_report(raw_report)
                    print(formatted_report['graph_name'])
                    Util.save_json(output_path, formatted_report['graph_name'], formatted_report)
            return_dict.clear()


if __name__ == '__main__':
    run_connected_graphs()
