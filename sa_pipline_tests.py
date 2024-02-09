from multiprocessing import Pool
import time
from src.sw.sa_pipeline.sa_pipeline_sw import SAPipeline
from src.util.per_graph import PeRGraph
from src.util.per_enum import ArchType
from src.util.util import Util


def run_connected_graphs():
    arch_types = [ArchType.ONE_HOP]
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
    dots_list = [[dot_connected_path + 'mac.dot', 'mac.dot']]

    # jobs_alive = []
    # manager = mp.Manager()
    # return_dict = manager.dict()
    task_counter = 0
    varst = []
    futures = []
    outputs = []
    pool = Pool()
    for th in total_threads:
        for arch_type in arch_types:
            local_counter = 0
            for dot_path, dot_name in dots_list:
                per_graph = PeRGraph(dot_path, dot_name)
                sa_pipeline = SAPipeline(per_graph, arch_type, distance_table_bits, make_shuffle, threads_per_copy)
                print("task:", task_counter, ",", "local_task:", local_counter)
                res = sa_pipeline.run(th // threads_per_copy, )
                # res = pool.apply_async(sa_pipeline.run, (th // threads_per_copy,))
                # res.wait()
                # print(res.ready())
                futures.append(res)
                local_counter += 1
    pool.close()
    pool.join()

    for output in futures:
        print(output.get())


if __name__ == '__main__':
    start_time = time.time()
    run_connected_graphs()
    end_time = time.time()
    print("Total time: " + str(end_time - start_time))
