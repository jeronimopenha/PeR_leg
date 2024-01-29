import os
from pathlib import Path
from src.sw.yoto_pipeline.yoto_pipeline_sw import YotoPipeline
from src.util.per_graph import PeRGraph
from src.util.util import Util
from src.util.per_enum import ArchType


def run_connected_graphs(test_name: str):
    # YOTO_1comp_counters TAG
    n_threads: int = 6
    seed: int = 0
    arch_type: ArchType = ArchType.ONE_HOP
    make_shuffle: bool = True
    distance_table_bits: int = 2

    root_path: str = Util.get_project_root()
    dot_path_base = root_path + '/dot_db/'
    dot_connected_path = dot_path_base + 'connected/'

    output_path_base = os.getcwd() + '/results/sw/yoto/yoto_pipeline/%s/' % arch_type

    # FIXME
    # output_path = output_path_base + test_name + '/'
    output_path = output_path_base

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # list connected benchmarks
    dots_list = Util.get_files_list_by_extension(dot_connected_path, '.dot')
    # FIXME a linha baixo e apenas para depuracao
    # dots_list = [['/home/jeronimo/Documentos/GIT/PeR/dot_db/connected/mac.dot', 'mac.dot']]
    for dot, dot_name in dots_list:
        per_graph = PeRGraph(dot)
        yoto = YotoPipeline(per_graph, arch_type, distance_table_bits, make_shuffle, n_threads, seed)
        results: dict = yoto.run(10)
        yoto.save_execution_report_json(results, output_path, dot_name)
        report = yoto.get_report(results, output_path, dot_name)
        box_plot_histogram: dict = {}
        for key in report['th_routed'].keys():
            if report['th_routed'][key]:
                box_plot_histogram[key] = report['th_histogram'][key]
        if box_plot_histogram:
            Util.get_router_boxplot_graph_from_dict(box_plot_histogram, output_path, dot_name)
        seed += 1


if __name__ == '__main__':
    run_connected_graphs('2024_01_23')
