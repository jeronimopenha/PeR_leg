import os
from src.python.sw.cgra.yott_pipeline.monte_carlo.yott_pipeline_mc1_sw import YOTTMC1Pipeline
from src.python.util.per_enum import ArchType
from src.python.util.per_graph import PeRGraph
from src.python.util.util import Util
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
        dot_connected_path = dot_path_base + 'graphs0_dag/'
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
            pipeline_method = YOTTMC1Pipeline(per_graph, arch_type, distance_table_bits, make_shuffle, [3,3,0.3],3,10)
            if run_parallel:
                raw_report: dict = pipeline_method.run_parallel(total_threads // threads_per_copy)
            else:
                raw_report: dict = pipeline_method.run_single(total_threads // threads_per_copy)
            raw_report['num_annotations'] = 3
            raw_report['method'] = 'MC1'
            limiars_str ='3,3,0.3'
            raw_report['limiar'] = limiars_str
            formatted_report = Util.get_formatted_report(raw_report)
            Util.save_json(output_path, dot_name.replace('.dot','')+f'-NA<{3}>-M<MC1={limiars_str}>.dot', formatted_report)
            reports.append(formatted_report)
if __name__ == '__main__':
    per = PeRGraph(Util.get_project_root() + "/dot_db/graphs0_dag/dag18-5x5.dot", "dag18-5x5.dot")
    yott = YOTTMC1Pipeline(per, ArchType.MESH, 4, True,  [3,3,0.3], 3, 10).run_single(1000)
    # run_connected_graphs()
