import os
from src.old.python.sw import YOTTXPipeline
from src.old.python.util.per_enum import ArchType
from src.old.python.util.per_graph import PeRGraph
from src.old.python import Util
run_parallel = False
def run_connected_graphs():
    archs_types = [ArchType.MESH, ArchType.ONE_HOP]
    for arch_type in archs_types:
        print(arch_type.name)
        print()
        threads_per_copy: int = 10
        total_threads: int = 100
        make_shuffle: bool = True
        distance_table_bits: int = 4

        root_path: str = Util.get_project_root()
        dot_path_base = root_path + '/dot_db/'
        dot_connected_path = dot_path_base + 'connected/'
        print(dot_connected_path)
        output_path_base = os.getcwd() + '/reports/sw/yott/yott_pipeline/t_%d/%s/' % (total_threads, arch_type)

        # output_path = output_path_base + test_name + '/'
        output_path = output_path_base

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # list connected benchmarks
        dots_list = Util.get_files_list_by_extension(dot_connected_path, '.dot')
        reports: list[dict] = []

        # FIXME the line below is only for debugging
        # dots_list = [[dot_connected_path + 'arf.dot', 'arf.dot']]
        for dot_path, dot_name in dots_list:
            per_graph = PeRGraph(dot_path, dot_name)
            print(per_graph.dot_name)
            pipeline_method = YOTTXPipeline(per_graph, arch_type, distance_table_bits, make_shuffle, 0.9,3,10)
            if run_parallel:
                raw_report: dict = pipeline_method.run_parallel(total_threads // threads_per_copy)
            else:
                raw_report: dict = pipeline_method.run_single(total_threads // threads_per_copy)
            raw_report['num_annotations'] = 3
            raw_report['method'] = 'X'
            raw_report['limiar'] = '0.9'
            formatted_report = Util.get_formatted_report(raw_report)
            Util.write_json(output_path, dot_name.replace('.dot', '') + f'-NA<{3}>-M<X=0.9>.dot', formatted_report)
            reports.append(formatted_report)
if __name__ == '__main__':
    # per = PeRGraph(Util.get_project_root() + "/dot_db/connected/mults1.dot", "mults1.dot")
    # yott = YOTTXPipeline(per, ArchType.MESH, 4, True, 0.9, 3, 10).run_single(100)
    run_connected_graphs()
