import os
import sys

base_path = os.getcwd()
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from src.sw.yoto_pipeline.yoto_pipeline_sw import YotoPipeline
from src.util.per_graph import PeRGraph
from src.util.util import Util as U


def run_connected_graphs(test_name: str):
    # YOTO_1comp_counters TAG
    n_threads = 6

    dot_path_base = os.getcwd() + '/dot_db/'
    dot_connected_path = dot_path_base + 'connected/'

    output_path_base = os.getcwd() + '/results/sw/yoto/yoto_pipeline/'

    output_path = output_path_base + test_name + '/'

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # list connected benchmarks
    dots_list = U.get_files_list_by_extension(dot_connected_path, '.dot')

    for dot, dot_name in dots_list:
        per_graph = PeRGraph(dot)
        yoto = YotoPipeline(per_graph, n_threads)
        results: dict = yoto.run(10)
        # yoto.save_execution_report_raw(results, output_path, dot_name)
        report = yoto.get_report(results, output_path, dot_name)
        box_plot_histogram: dict = {}
        for key in report['th_routed'].keys():
            if report['th_routed'][key]:
                box_plot_histogram[key] =report['th_histogram'][key]
        U.get_router_hist_graph_from_dict(box_plot_histogram)


if __name__ == '__main__':
    run_connected_graphs('2024_01_17')
