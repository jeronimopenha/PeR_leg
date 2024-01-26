from src.util.per_graph import PeRGraph
from src.util.util import Util
from src.util.per_enum import ArchType
from src.util.traversal import Traversal
from src.sw.yoto_pipeline.stage1_yoto import Stage1YOTO
from src.sw.yoto_pipeline.stage2_yoto import Stage2YOTO
from src.sw.yoto_pipeline.stage3_yoto import Stage3YOTO
from src.sw.yoto_pipeline.stage4_yoto import Stage4YOTO
from src.sw.yoto_pipeline.stage5_yoto import Stage5YOTO


class YotoPipeline(Traversal):
    def __init__(self, per_graph: PeRGraph, arch_type: ArchType, distance_table_bits: int, make_shuffle: bool,
                 n_threads: int = 1, random_seed: int = 0):
        super().__init__(per_graph, arch_type, distance_table_bits, make_shuffle, n_threads, random_seed)

    def run(self, n_copies: int = 1) -> dict:
        results: dict = {}
        # print(self.per_graph.nodes)
        # print(self.per_graph.neighbors)
        # print()
        self.reset_random(0)
        for t in range(n_copies):
            results_key = 'exec_%d' % t
            results[results_key] = {}

            first_nodes: list = [self.edges_int[i][0][0] for i in range(self.len_pipeline)]
            n2c, c2n = self.get_initial_position_ij(first_nodes, self.len_pipeline)

            st1_edge_sel: Stage1YOTO = Stage1YOTO(self.n_threads, self.n_edges, self.len_pipeline)
            st2_edges: Stage2YOTO = Stage2YOTO(self.edges_int, self.n_edges)
            st3_n2c: Stage3YOTO = Stage3YOTO(n2c, self.per_graph.n_cells_sqrt, self.len_pipeline)
            st4_dist = Stage4YOTO(self.arch_type, self.per_graph.n_cells_sqrt, self.len_pipeline, self.make_shuffle)
            st5_c2n = Stage5YOTO(c2n, self.per_graph.n_cells_sqrt)

            counter = 0
            while not st1_edge_sel.done:
                st1_edge_sel.compute(st1_edge_sel.old_output, st5_c2n.old_output)
                st2_edges.compute(st1_edge_sel.old_output)
                st3_n2c.compute(st2_edges.old_output, st5_c2n.old_output)
                st4_dist.compute(st3_n2c.old_output)
                st5_c2n.compute(st4_dist.old_output, st5_c2n.old_output)
                counter += 1

            results[results_key]['total_exec_clk'] = st1_edge_sel.total_pipeline_counter
            th_dict: dict = {}
            for th in range(self.len_pipeline):
                th_key = 'Exec_%d_TH_%d' % (t, th)
                th_dict[th_key]: dict = {}
                th_dict[th_key]['total_th_clk'] = st1_edge_sel.exec_counter[th]
                th_dict[th_key]['th_placement'] = st3_n2c.n2c[th]

                graph_edges_str = self.per_graph.edges_str
                graph_edges_int = self.get_edges_int(graph_edges_str)
                dic_edges_dist, list_edges_dist = self.get_edges_distances(graph_edges_int, st3_n2c.n2c[th])
                dic_edges_dist = dict(sorted(dic_edges_dist.items(), key=lambda x: x[1]))
                th_dict[th_key]['th_placement_distances'] = dic_edges_dist

                router_edges = [graph_edges_int[i] for i in
                                sorted(range(len(list_edges_dist)), key=lambda i: list_edges_dist[i])]

                routed, grid, dic_path = self.routing_mesh(router_edges, st3_n2c.n2c[th])
                histogram: dict = {}
                for path in dic_path.keys():
                    path_len = len(dic_path[path])
                    len_key = 'dist_%d' % path_len
                    if len_key in histogram:
                        histogram[len_key] += 1
                    else:
                        histogram[len_key] = 1
                th_dict[th_key]['th_routed'] = routed
                th_dict[th_key]['th_histogram'] = dict(sorted(histogram.items()))
            results[results_key]['th_results'] = th_dict
        return results

    def save_execution_report_json(self, results: dict, path: str, file_name: str) -> None:
        execution_report_raw: dict = self.get_report(results, path, file_name)

        Util.save_json(path, file_name, execution_report_raw)

    def get_report(self, results: dict, path: str, file_name: str) -> dict:
        exec_max_clk: int = -1
        exec_min_clk: int = -1
        exec_avg_clk: int = 0
        n_tests = len(results)
        th_max_clk: int = -1
        th_min_clk: int = -1
        th_avg_clk: int = 0
        # Total threads quantity
        n_threads: int = n_tests * self.n_threads
        th_histogram: dict = {}
        th_routed: dict = {}
        th_placement_distances: dict = {}

        # generate data for reports
        for result_key in results.keys():
            result = results[result_key]

            total_exec_clk: int = result['total_exec_clk']

            exec_avg_clk += total_exec_clk

            if exec_max_clk == -1:
                exec_max_clk = total_exec_clk
            else:
                if total_exec_clk > exec_max_clk:
                    exec_max_clk = total_exec_clk
            if exec_min_clk == -1:
                exec_min_clk = total_exec_clk
            else:
                if total_exec_clk < exec_min_clk:
                    exec_min_clk = total_exec_clk
            for th_key in result['th_results'].keys():
                th_results = result['th_results'][th_key]
                # th_placements[th_key] = th_results['th_placement']
                th_histogram[th_key] = th_results['th_histogram']
                th_routed[th_key] = th_results['th_routed']
                th_placement_distances[th_key] = th_results['th_placement_distances']

                total_th_clk: int = th_results['total_th_clk']

                th_avg_clk += total_th_clk

                if th_max_clk == -1:
                    th_max_clk = total_th_clk
                else:
                    if total_th_clk > th_max_clk:
                        th_max_clk = total_th_clk
                if th_min_clk == -1:
                    th_min_clk = total_th_clk
                else:
                    if total_th_clk < th_min_clk:
                        th_min_clk = total_th_clk
        exec_avg_clk /= n_tests
        th_avg_clk /= n_threads

        execution_report_raw: dict = {
            'graph_name': file_name,
            'graph_path': path,
            'n_tests': n_tests,
            'exec_max_clk': exec_max_clk,
            'exec_min_clk': exec_min_clk,
            'exec_avg_clk': exec_avg_clk,
            'th_max_clk': th_max_clk,
            'th_min_clk': th_min_clk,
            'th_avg_clk': th_avg_clk,
            'n_threads': n_threads,
            'th_routed': th_routed,
            'th_histogram': th_histogram,
            'th_placement_distances': th_placement_distances,
            'nodes_dict': self.per_graph.nodes_to_idx,
        }
        return execution_report_raw
