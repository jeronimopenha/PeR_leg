import os
from src.sw.yott_pipeline.yott_pipeline_sw import YOTTPipeline
from src.sw.yoto_pipeline.yoto_pipeline_sw import YotoPipeline

from src.util.per_enum import ArchType
from src.util.per_graph import PeRGraph
from src.util.util import Util

methods = [YotoPipeline, YOTTPipeline]
path_results = ["yoto/yoto_pipeline","yott/yott_pipeline"]

arch_types = [ ArchType.MESH, ArchType.ONE_HOP]
root_path: str = Util.get_project_root()
dot_path_base = root_path + '/dot_db/'
dot_connected_path = dot_path_base + 'connected/'
make_shuffle: bool = True
distance_table_bits: int = 2
copies = [1,10,100]
for i,method in enumerate(methods):
    for arch_type in arch_types:        
        len_pipe = method.len_pipeline
        total_executions = [len_pipe * copy for copy in copies]
        for total_execution in total_executions:
            print()
            print(method.__name__,arch_type,total_execution)
            print()
            threads_per_copy: int = len_pipe
            seed: int = 0

            output_path_base = os.getcwd() + '/results/sw/%s/t_%d/%s/' % (path_results[i],total_execution, arch_type)

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
                pipeline_method = method(per_graph, arch_type, distance_table_bits,make_shuffle,len_pipe,seed)
                raw_report: dict = pipeline_method.run(total_execution // threads_per_copy)
                formatted_report = Util.get_formatted_report(raw_report)
                Util.save_json(output_path, dot_name,formatted_report)
                reports.append(formatted_report)
                seed += 1