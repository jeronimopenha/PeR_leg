from src.util.per_graph import PeRGraph
from src.util.util import Util as U
from src.util.yoto.yoto import Yoto
from src.sw.yoto_pipeline.st1_edges_sel import St1EdgesSel
from src.sw.yoto_pipeline.st2_edges import St2Edges
from src.sw.yoto_pipeline.st3_n2c import St3N2C
from src.sw.yoto_pipeline.st4_dist import St4Dist
from src.sw.yoto_pipeline.st5_c2n import St5C2n


class YotoPipeline(Yoto):
    def __init__(self, per_graph: PeRGraph, n_threads: int = 1):
        super().__init__(per_graph, n_threads)

    def run(self, n_copies: int = 1) -> dict:
        results: dict = {}
        print(self.per_graph.nodes)
        print(self.per_graph.neighbors)
        print()
        for t in range(n_copies):
            results_key = 'exec_%d' % t
            results[results_key] = {}

            n2c, c2n = self.get_initial_position_ij(self.edges_int[0][0], self.latency)

            st1_edge_sel: St1EdgesSel = St1EdgesSel(self.n_threads, self.per_graph.n_edges, self.latency)
            st2_edges: St2Edges = St2Edges(self.edges_int, self.latency, self.per_graph.n_edges)
            st3_n2c: St3N2C = St3N2C(n2c, self.per_graph.n_cells_sqrt, self.latency)
            st4_dist = St4Dist(self.per_graph.n_cells_sqrt)
            st5_c2n = St5C2n(c2n, self.per_graph.n_cells_sqrt)

            counter = 0
            while not st1_edge_sel.done:
                st1_edge_sel.compute(st1_edge_sel.output, st5_c2n.output)
                st2_edges.compute(st1_edge_sel.output)
                st3_n2c.compute(st2_edges.output, st5_c2n.output)
                st4_dist.compute(st3_n2c.output, st4_dist.output)
                st5_c2n.compute(st4_dist.output, st5_c2n.output)
                counter += 1

            results[results_key]['total_exec_clk'] = st1_edge_sel.total_pipeline_counter
            th_dict: dict = {}
            for th in range(self.latency):
                th_key = 'Copy_%d_TH_%d' % (t, th)
                th_dict[th_key]: dict = {}
                th_dict[th_key]['total_th_clk'] = st1_edge_sel.exec_counter[th]
                th_dict[th_key]['th_placement'] = st3_n2c.n2c[th]

                routed, grid, dic_path = self.routing_mesh(self.edges_int, st3_n2c.n2c[th])
                histogram: dict = {}
                for path in dic_path.keys():
                    path_len = len(dic_path[path])
                    if path_len in histogram:
                        histogram[path_len] += 1
                    else:
                        histogram[path_len] = 1
                th_dict[th_key]['th_routed'] = routed
                th_dict[th_key]['th_histogram'] = dict(sorted(histogram.items()))
            results[results_key]['th_results'] = th_dict
        return results

    def save_execution_report_raw(self, results: dict, path: str, file_name: str) -> None:
        execution_report_raw: dict = self.get_report(results, path, file_name)

        U.save_json(path, file_name, execution_report_raw)

    def get_report(self, results: dict, path: str, file_name: str) -> dict:
        total_max_clk: int = -1
        total_min_clk: int = -1
        total_avg_clk: int = 0
        n_tests = len(results)
        th_max_clk: int = -1
        th_min_clk: int = -1
        th_avg_clk: int = 0
        total_threads: int = n_tests * self.n_threads
        th_histogram: dict = {}
        th_routed: dict = {}

        # generate data for reports
        for r_key in results.keys():
            result = results[r_key]

            total_exec_clk: int = result['total_exec_clk']

            total_avg_clk += total_exec_clk

            if total_max_clk == -1:
                total_max_clk = total_exec_clk
            else:
                if total_exec_clk > total_max_clk:
                    total_max_clk = total_exec_clk
            if total_min_clk == -1:
                total_min_clk = total_exec_clk
            else:
                if total_exec_clk < total_min_clk:
                    total_min_clk = total_exec_clk
            for th_key in result['th_results'].keys():
                th_results = result['th_results'][th_key]
                # th_placements[th_key] = th_results['th_placement']
                th_histogram[th_key] = th_results['th_histogram']
                th_routed[th_key] = th_results['th_routed']

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
        total_avg_clk /= n_tests
        th_avg_clk /= total_threads

        execution_report_raw: dict = {
            'graph_name': file_name,
            'graph_path': path,
            'n_tests': n_tests,
            'total_max_clk': total_max_clk,
            'total_min_clk': total_min_clk,
            'total_avg_clk': total_avg_clk,
            'th_max_clk': th_max_clk,
            'th_min_clk': th_min_clk,
            'th_avg_clk': th_avg_clk,
            'total_threads': total_threads,
            'th_routed': th_routed,
            'th_histogram': th_histogram,
            'nodes_dict': self.per_graph.nodes_to_idx,
        }
        return execution_report_raw
