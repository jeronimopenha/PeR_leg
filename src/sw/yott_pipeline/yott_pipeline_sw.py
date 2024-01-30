from src.util.per_graph import PeRGraph
from src.sw.yott_pipeline.FIFOQueue import FIFOQueue
from src.sw.yott_pipeline.stage0_yott import Stage0YOTT

from src.sw.yott_pipeline.stage0_yott import Stage0YOTT
from src.sw.yott_pipeline.stage1_yott import Stage1YOTT
from src.sw.yott_pipeline.stage2_yott import Stage2YOTT
from src.sw.yott_pipeline.stage3_yott import Stage3YOTT
from src.sw.yott_pipeline.stage4_yott import Stage4YOTT
from src.sw.yott_pipeline.stage5_yott import Stage5YOTT
from src.sw.yott_pipeline.stage6_yott import Stage6YOTT
from src.util.traversal import Traversal
from src.util.util import Util

class YOTTPipeline(Traversal):
    def __init__(self,per_graph: PeRGraph,arch_type,distance_table_bits, make_shuffle, num_threads: int = 7):
        super().__init__(per_graph, arch_type,distance_table_bits,make_shuffle,7,num_threads)
        self.len_edges = len(self.edges_int[0])
        # print(self.annotations)
        # input()
        #FIXME retirar
        # self.annotations = [[[-1,-1] for i in range(self.len_edges)] for j in range(self.n_threads)]



    def run(self, n_copies: int = 1) -> dict:

        # print(self.per_graph.nodes)
        # print(self.per_graph.neighbors)
        # print()
        raw_report: dict = {}
        self.reset_random(0)
        for t in range(n_copies):
            results_key = 'exec_%d' % t
            raw_report[results_key] = {}

            first_nodes: list = [self.edges_int[i][0][0] for i in range(self.len_pipeline)]
            N2C, C2N = self.get_initial_position_ij(first_nodes, self.len_pipeline)
            
            stage0 = Stage0YOTT(FIFOQueue(self.n_threads),self.len_pipeline)
            # FIXME zigzag deve conter apenas arestas que mapeiam todos os nós
            stage1 = Stage1YOTT(self.len_pipeline,self.n_threads,self.len_edges)
            stage2 = Stage2YOTT(self.edges_int,self.per_graph,self.annotations,self.n_threads)
            stage4 = Stage4YOTT(self.per_graph.n_cells_sqrt,self.len_pipeline,self.distance_table_bits, self.make_shuffle)
            stage3 = Stage3YOTT(self.len_pipeline,N2C)
            stage5 = Stage5YOTT(self.arch_type)
            stage6 = Stage6YOTT(self.per_graph.n_cells_sqrt,self.len_pipeline,C2N)

            len_adjacentes_indexes = len(stage4.distance_table[0])

            counter = 0
            while not stage1.done:
                # print(stage6.old_output_stage3)
                stage0.compute()
                # print(stage0.new_output)
                # print()
                # print(stage0.old_output)
                stage1.compute(stage0)
                # print(stage1.new_output)
                # print()
                # print(stage1.old_output)
                stage2.compute(stage1)
                # print(stage2.new_output)
                # print()
                # print(stage2.old_output)
                stage3.compute(stage2,stage6,len_adjacentes_indexes)
                # print(stage3.new_output)
                # print()
                # print(stage3.old_output)
                # print(stage6.C2N)
                stage4.compute(stage3)
                # print(stage4.new_output)
                # print()
                # print(stage4.old_output)
                stage5.compute(stage4)
                # print(stage5.new_output)
                # print()
                # print(stage5.old_output)
                stage6.compute(stage5,stage0)
                # print(stage6.new_output_stage3)
                # print()
        
                # input()
                counter += 1
            # self.print_grid(stage6.C2N)

            raw_report[results_key]['total_exec_clk'] = stage0.total_pipeline_counter
            raw_report[results_key]['arch_type'] = self.arch_type
            raw_report[results_key]['total_edges'] = self.total_edges
            raw_report[results_key]['edges_visited'] = self.visited_edges
            raw_report[results_key]['n_cells'] = self.per_graph.n_cells
            raw_report[results_key]['n_cells_sqrt'] = self.per_graph.n_cells_sqrt
            th_dict: dict = {}
            for th in range(self.len_pipeline):
                th_key = 'Exec_%d_TH_%d' % (t, th)
                th_dict[th_key]: dict = {}
                th_dict[th_key]['total_th_clk'] = stage0.exec_counter[th]
                th_dict[th_key]['th_placement'] = stage3.N2C[th]

                graph_edges_str = self.per_graph.edges_str
                graph_edges_int = self.get_edges_int(graph_edges_str)
                dic_edges_dist, list_edges_dist = Util.get_edges_distances(self.arch_type, graph_edges_int,
                                                                           stage3.N2C[th])
                dic_edges_dist = dict(sorted(dic_edges_dist.items(), key=lambda x: x[1]))
                th_dict[th_key]['th_placement_distances'] = dic_edges_dist

                '''router_edges = [graph_edges_int[i] for i in
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
                th_dict[th_key]['th_routed'] = routed'''
                # th_dict[th_key]['th_histogram'] = dict(sorted(histogram.items()))
            raw_report[results_key]['th_results'] = th_dict

        return raw_report

    def get_formatted_report(self, formatted_report: dict, path: str, file_name: str) -> dict:
        exec_max_clk: int = -1
        exec_min_clk: int = -1
        exec_avg_clk: int = 0
        exec_total_edges: int = formatted_report['exec_0']['total_edges']
        exec_visited_edges: int = formatted_report['exec_0']['edges_visited']
        n_cells: int = formatted_report['exec_0']['n_cells']
        n_cells_sqrt: int = formatted_report['exec_0']['n_cells_sqrt']
        n_tests = len(formatted_report)
        th_max_clk: int = -1
        th_min_clk: int = -1
        th_avg_clk: int = 0
        # Total threads quantity
        n_threads: int = n_tests * self.n_threads
        # th_histogram: dict = {}
        # th_routed: dict = {}
        th_placement_distances: dict = {}

        # generate data for reports
        for report_key in formatted_report.keys():
            report = formatted_report[report_key]

            total_exec_clk: int = report['total_exec_clk']

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
            for th_key in report['th_results'].keys():
                th_results = report['th_results'][th_key]
                # th_placements[th_key] = th_results['th_placement']
                # th_histogram[th_key] = th_results['th_histogram']
                # th_routed[th_key] = th_results['th_routed']
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

        formatted_report: dict = {
            'graph_name': file_name,
            'graph_path': path,
            'total_edges': exec_total_edges,
            'visited_edges': exec_visited_edges,
            'n_tests': n_tests,
            'n_cells': n_cells,
            'n_cells_sqrt': n_cells_sqrt,
            'exec_max_clk': exec_max_clk,
            'exec_min_clk': exec_min_clk,
            'exec_avg_clk': exec_avg_clk,
            'th_max_clk': th_max_clk,
            'th_min_clk': th_min_clk,
            'th_avg_clk': th_avg_clk,
            'n_threads': n_threads,
            # 'th_routed': th_routed,
            # 'th_histogram': th_histogram,
            'th_placement_distances': th_placement_distances,
            'nodes_dict': self.per_graph.nodes_to_idx,
        }
        return formatted_report

    def print_grid(self,C2N):
        for idx_thread,thread in enumerate(C2N):
            print(f'thread{idx_thread}')
            for row in thread:
                print(row)
            print()
