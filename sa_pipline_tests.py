import os
import multiprocessing as mp
import time
from src.sw.sa_pipeline.sa_pipeline_sw import SAPipeline
from src.util.per_graph import PeRGraph
from src.util.per_enum import ArchType
from src.util.util import Util


def run_connected_graphs():
    arch_types = [ArchType.ONE_HOP, ArchType.MESH]
    total_threads = [6]

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
    PROCESSES = 7

    tasks = []
    jobs_alive = []
    for arch_type in arch_types:
        tasks.clear()
        for th in total_threads:
            manager = mp.Manager()
            return_dict = manager.dict()
            output_path = ""
            for dot_path, dot_name in dots_list:
                per_graph = PeRGraph(dot_path, dot_name)
                print(dot_name, arch_type, th)
                output_path = Util.get_project_root() + '/reports/sw/sa/sa_pipeline/t_%d/%s/' % (th, arch_type)
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                sa_pipeline = SAPipeline(per_graph, arch_type, distance_table_bits, make_shuffle, threads_per_copy)
                tasks.append([sa_pipeline, th // threads_per_copy])
            for task_counter, task in enumerate(tasks):
                p = mp.Process(target=task[0].run,
                               args=(str(task_counter % PROCESSES), return_dict, task[1],))
                jobs_alive.append(p)
                p.start()
                while len(jobs_alive) > PROCESSES:
                    jobs_alive = [job for job in jobs_alive if job.is_alive()]
                    time.sleep(1)
            while len(jobs_alive) > 0:
                jobs_alive = [job for job in jobs_alive if job.is_alive()]
                time.sleep(1)
            for j_name in return_dict.keys():
                print(j_name)  # , return_dict[j_name])
                raw_report: dict = return_dict[j_name]
                formatted_report = Util.get_formatted_report(raw_report)
                # Util.save_json(output_path, dot_name, formatted_report)
                '''for res in return_dict[j_name]:
                    r_list.append(res)
                return_dict[j_name] = []'''


# raw_report: dict = sa_pipeline.run(total_threads // threads_per_copy)
# formatted_report = Util.get_formatted_report(raw_report)
# Util.save_json(output_path, dot_name, formatted_report)
# print(return_list)
# a = 1


if __name__ == '__main__':
    run_connected_graphs()
