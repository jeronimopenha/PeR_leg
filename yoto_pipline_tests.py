import os
from src.sw.yoto_pipeline.yoto_pipeline_sw import YotoPipeline
from src.util.per_graph import PeRGraph
from src.util.util import Util
from src.util.per_enum import ArchType


def run_connected_graphs():
    # YOTO_1comp_counters TAG
    threads_per_copy: int = 6
    total_threads: int = 6
    seed: int = 0
    arch_type: ArchType = ArchType.ONE_HOP
    make_shuffle: bool = True
    distance_table_bits: int = 4

    root_path: str = Util.get_project_root()
    dot_path_base = root_path + '/dot_db/'
    dot_connected_path = dot_path_base + 'connected/'

    output_path_base = os.getcwd() + '/results/sw/yoto/yoto_pipeline/t_%d/%s/' % (total_threads, arch_type)

    # FIXME
    # output_path = output_path_base + test_name + '/'
    output_path = output_path_base

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # list connected benchmarks
    dots_list = Util.get_files_list_by_extension(dot_connected_path, '.dot')
    # FIXME a linha baixo e apenas para depuracao
    dots_list = [[dot_connected_path + 'arf.dot', 'arf.dot']]
    for dot_path, dot_name in dots_list:
        per_graph = PeRGraph(dot_path, dot_name)
        Util.get_graph_annotations(per_graph)
        print(per_graph.dot_name)
        yoto_pipeline_sw = YotoPipeline(per_graph, arch_type, distance_table_bits, make_shuffle, threads_per_copy, seed)
        raw_report: dict = yoto_pipeline_sw.run(total_threads // threads_per_copy)
        formatted_report = yoto_pipeline_sw.get_formatted_report(raw_report, output_path, dot_name)
        Util.save_execution_report_json(formatted_report, output_path, dot_name)

        min_distance: int = per_graph.n_edges * per_graph.n_cells
        edges_g0: int = per_graph.n_edges
        for rkey in raw_report['th_placement_distances'].keys():
            total_dist: int = 0
            edg = 0
            for dist_k in raw_report['th_placement_distances'][rkey].keys():
                d = raw_report['th_placement_distances'][rkey][dist_k] - 1
                if d > 0:
                    edg += 1
                total_dist += d
            if total_dist < min_distance:
                min_distance = total_dist
                edges_g0 = edg
        print(min_distance, ';', edges_g0)
        # print(edges_g0)
        a = 1
        # box_plot_histogram: dict = {}
        '''for key in report['th_routed'].keys():
            if report['th_routed'][key]:
                box_plot_histogram[key] = report['th_histogram'][key]
        if box_plot_histogram:
            Util.get_router_boxplot_graph_from_dict(box_plot_histogram, output_path, dot_name)'''
        seed += 1


if __name__ == '__main__':
    run_connected_graphs()
