import os
from src.sw.yott_pipeline.yott_pipeline_sw import YOTTPipeline
from src.util.per_enum import ArchType
from src.util.per_graph import PeRGraph
from src.util.util import Util


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
            yott_pipeline_sw = YOTTPipeline(per_graph, arch_type, distance_table_bits, make_shuffle, 3)
            raw_report: dict = yott_pipeline_sw.run(total_threads // threads_per_copy)
            formatted_report = Util.get_formatted_report(raw_report)
            Util.save_json(output_path, dot_name, formatted_report)
            reports.append(formatted_report)



if __name__ == '__main__':
    per = PeRGraph("/home/fabio/Mestrado/PeR/dot_db/graphs0/14-4x4.dot","14-4x4.dot")
    yott = YOTTPipeline(per,ArchType.MESH,4,True,3,1).run(1)
    # run_connected_graphs()
