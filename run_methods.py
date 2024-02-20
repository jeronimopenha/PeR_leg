import os
from src.sw.yott_pipeline.yott_pipeline_sw import YOTTPipeline
from src.sw.yoto_pipeline.yoto_pipeline_sw import YotoPipelineSw

from src.util.per_enum import ArchType
from src.util.per_graph import PeRGraph
from src.util.util import Util
import time

methods = [YOTTPipeline, YotoPipelineSw]
path_results = ["yott/yott_pipeline", "yoto/yoto_pipeline"]

run_parallel = True
arch_types = [ArchType.MESH, ArchType.ONE_HOP]
root_path: str = Util.get_project_root()
dot_path_base = root_path + '/dot_db/'
dot_connected_paths = [dot_path_base + path_graph for path_graph in ['connected/','graphs0_dag/','graphs1_dag/','graphs0_tree/','graphs1_tree/']]
make_shuffle: bool = True
distance_table_bits: int = 4
copies = [1,10,100]

start = time.time()
for dot_connected_path in dot_connected_paths:
    for i, method in enumerate(methods):
        for arch_type in arch_types:
            len_pipe = method.len_pipeline
            total_executions = [len_pipe * copy for copy in copies]
            for total_execution in total_executions:
                print()
                print(method.__name__, arch_type, total_execution)
                print()
                threads_per_copy: int = len_pipe

                output_path_base = Util.get_project_root() + '/reports/sw/%s/t_%d/%s/' % (
                    path_results[i], total_execution, arch_type.name)

                # output_path = output_path_base + test_name + '/'
                output_path = output_path_base

                if not os.path.exists(output_path):
                    os.makedirs(output_path)

                # list connected benchmarks
                dots_list = Util.get_files_list_by_extension(dot_connected_path, '.dot')
                # dots_list = [
                #    [dot_connected_path + "tree 10 - 4x4 - Inv.dot - MC = 1.dot", "tree 10 - 4x4 - Inv.dot - MC = 1.dot"]]
                reports: list[dict] = []

                # FIXME the line below is only for debugging
                # dots_list = [[dot_connected_path + 'arf.dot', 'arf.dot']]
                num_annotations = [1,2,3] if method == YOTTPipeline else [0]
                for num_annotation in num_annotations:
                    for dot_path, dot_name in dots_list:
                        per_graph = PeRGraph(dot_path, dot_name)
                        print(per_graph.dot_name)
                        if method == YotoPipelineSw:
                            pipeline_method = YotoPipelineSw(per_graph, arch_type, distance_table_bits, make_shuffle, len_pipe)
                        elif method == YOTTPipeline:
                            pipeline_method = YOTTPipeline(per_graph, arch_type, distance_table_bits, make_shuffle, num_annotation, len_pipe)
                        if run_parallel:
                            raw_report: dict = pipeline_method.run_parallel(total_execution // threads_per_copy)
                        else:
                            raw_report: dict = pipeline_method.run_single(total_execution // threads_per_copy)
                        raw_report['num_annotations'] = num_annotation
                        formatted_report = Util.get_formatted_report(raw_report)
                        Util.save_json(output_path, dot_name.replace('.dot','')+f'-NA<{num_annotation}>.dot', formatted_report)
                        reports.append(formatted_report)
end = time.time()

print(f'elapsed time = {end - start}')
