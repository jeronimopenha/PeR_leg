from math import ceil
import os
import pandas as pd
import json
import traceback
import random
from pathlib import Path
from src.util.per_enum import ArchType
from src.util.per_graph import PeRGraph
import matplotlib

# from src.util.traversal import Traversal

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class Util(object):

    @staticmethod
    def get_formatted_report( raw_report: dict) -> dict:
        exec_max_clk: int = -1
        exec_min_clk: int = -1
        exec_avg_clk: int = 0
        n_copies = raw_report['n_copies']
        th_max_clk: int = -1
        th_min_clk: int = -1
        th_avg_clk: int = 0
        # Total threads quantity
        total_threads: int = raw_report['total_threads']
        th_placement_distances: dict = {}

        # generate data for reports
        for report_key in raw_report['reports'].keys():
            report = raw_report['reports'][report_key]

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
        exec_avg_clk /= n_copies
        th_avg_clk /= total_threads

        formatted_report = raw_report.copy()
        del formatted_report['reports']
        del formatted_report['nodes_dict']
        formatted_report["exec_max_clk"] = exec_max_clk
        formatted_report["exec_min_clk"] = exec_min_clk
        formatted_report["exec_avg_clk"] = exec_avg_clk
        formatted_report["th_max_clk"] = th_max_clk
        formatted_report["th_min_clk"] = th_min_clk
        formatted_report["th_avg_clk"] = th_avg_clk
        formatted_report["th_placement_distances"] = th_placement_distances
        formatted_report['nodes_dict'] = raw_report['nodes_dict']

        return formatted_report

    @staticmethod
    def create_report(traversal, algorithm: str, n_copies: int, reports: dict) -> dict:
        exec_report: dict = {
            "graph_name": traversal.per_graph.dot_name,
            "algorithm": algorithm,
            "arch_type": traversal.arch_type.name,
            "total_edges": traversal.total_edges,
            "visited_edges": traversal.visited_edges,
            "n_copies": n_copies,
            "total_threads": traversal.n_threads * n_copies,
            "n_cells": traversal.per_graph.n_cells,
            "n_lines": traversal.n_lines,
            "n_columns": traversal.n_columns,
            "reports": reports,
            "nodes_dict": traversal.per_graph.nodes_to_idx
        }
        return exec_report

    @staticmethod
    def create_exec_report(traversal, exec_num: int, total_pipeline_counter: int, exec_counter: list,
                           n2c: list[list[list]]):
        exec_report: dict = {
            'total_exec_clk': total_pipeline_counter
        }
        th_dict: dict = {}
        for th in range(traversal.len_pipeline):
            th_key = 'Exec_%d_TH_%d' % (exec_num, th)
            th_dict[th_key]: dict = {}
            th_dict[th_key]['total_th_clk'] = exec_counter[th]
            th_dict[th_key]['th_placement'] = n2c[th]
            edges_str = traversal.edges_str
            edges_int = traversal.get_edges_int(edges_str[th])
            dic_edges_dist = Util.get_edges_distances(traversal.arch_type, edges_int, n2c[th])[0]
            dic_edges_dist = dict(sorted(dic_edges_dist.items(), key=lambda x: x[1]))
            th_dict[th_key]['th_placement_distances'] = dic_edges_dist
        exec_report['th_results'] = th_dict
        return exec_report

    @staticmethod
    def get_project_root() -> str:
        path = Path(__file__).parent.parent.parent
        return str(path)

    @staticmethod
    def get_line_column_list_sqrt(cells: list, cells_sqrt: int) -> list[tuple[int, int]]:
        return Util.get_line_column_list(cells, cells_sqrt, cells_sqrt)

    @staticmethod
    def get_line_column_list(cells: list, n_lines: int, n_columns: int) -> list[tuple[int, int]]:
        line_column_list: list = []
        for cell in cells:
            line_column_list.append(Util.get_line_column_cell(cell, n_lines, n_columns))
        return line_column_list

    @staticmethod
    def get_line_column_cell_sqrt(cell: int, cells_sqrt: int) -> tuple[int, int]:
        return Util.get_line_column_cell(cell, cells_sqrt, cells_sqrt)

    @staticmethod
    def get_line_column_cell(cell: int, n_lines: int, n_columns: int) -> tuple[int, int]:
        line: int = cell // n_lines
        column: int = cell % n_columns
        return line, column

    @staticmethod
    def get_distance_table(arch_type: ArchType, cells_sqrt: int, make_shuffle: bool) -> list[list]:
        if arch_type == ArchType.MESH:
            return Util.get_mesh_distances(cells_sqrt, make_shuffle)
        elif arch_type == ArchType.ONE_HOP:
            return Util.get_one_hop_distances(cells_sqrt, make_shuffle)
        else:
            raise Exception("Architecture type not supported")

    @staticmethod
    def get_mesh_distances(cells_sqrt: int, make_shuffle: bool) -> list[list]:
        distance_table_raw: list[list] = [[] for i in range((cells_sqrt - 1) * 2)]
        for i in range(cells_sqrt):
            for j in range(cells_sqrt):
                if j == i == 0:
                    continue
                d: int = i + j
                if [i, j] not in distance_table_raw[d - 1]:
                    distance_table_raw[d - 1].append([i, j])
                if [i, -j] not in distance_table_raw[d - 1]:
                    distance_table_raw[d - 1].append([i, -j])
                if [-i, -j] not in distance_table_raw[d - 1]:
                    distance_table_raw[d - 1].append([-i, -j])
                if [-i, j] not in distance_table_raw[d - 1]:
                    distance_table_raw[d - 1].append([-i, j])
        mesh_distances: list[list] = Util.format_distance_table(distance_table_raw, make_shuffle)
        return mesh_distances

    @staticmethod
    def get_one_hop_distances(cells_sqrt: int, make_shuffle: bool) -> list[list]:
        max_distance: int = 2 * ceil((cells_sqrt - 1) / 2)
        distance_table_raw: list[list] = [[] for i in range(max_distance + 1)]
        for i in range(cells_sqrt):
            di: int = ceil(i / 2)
            for j in range(cells_sqrt):
                dj: int = ceil(j / 2)
                d: int = di + dj
                if d == 0:
                    continue
                distance_table_raw[d - 1].append([i, j])
                if i == 0:
                    distance_table_raw[d - 1].append([i, -j])
                elif j == 0:
                    distance_table_raw[d - 1].append([-i, j])
                else:
                    distance_table_raw[d - 1].append([i, -j])
                    distance_table_raw[d - 1].append([-i, j])
                    distance_table_raw[d - 1].append([-i, -j])

        one_hop_distances: list[list] = Util.format_distance_table(distance_table_raw, make_shuffle)
        return one_hop_distances

    @staticmethod
    def format_distance_table(distance_table_raw: list[list], make_shuffle: bool) -> list[list]:
        one_hop_distances: list[list] = []
        for d in range(len(distance_table_raw)):
            if make_shuffle:
                random.shuffle(distance_table_raw[d])
            for p in distance_table_raw[d]:
                one_hop_distances.append(p)
        return one_hop_distances

    @staticmethod
    def get_cell_from_line_column(cell_line: int, cell_column: int, n_lines: int) -> int:
        cell: int = cell_line * n_lines + cell_column

        return cell

    @staticmethod
    def get_files_list_by_extension(path: str, file_extension: str) -> list[list]:
        files_list_by_extension = [[os.path.join(file_path, file_name), file_name] for file_path, dir_name, filenames in
                                   os.walk(path) for file_name in filenames if
                                   os.path.splitext(file_name)[1] == file_extension]
        # files_path_list = [[os.path.join(path, name), name] for name in os.listdir(path)]
        # files_list = [file for file in files_path_list if os.path.isfile(file[0])]
        # files_list_by_extension = [arq for arq in files_list if arq[0].lower().endswith(file_extension)]
        return files_list_by_extension

    @staticmethod
    def read_json(file: str):
        with open(file) as p_file:
            contents: str = p_file.read()
            content_dic: dict = json.loads(contents)
        p_file.close()
        return content_dic

    @staticmethod
    def save_json(path: str, file_name: str, data: dict):
        with open(path + file_name + '.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        file.close()

    @staticmethod
    def get_router_boxplot_graph_from_dict(report_data: dict, graph_path: str, graph_name: str):
        data: dict = {}
        for router_reports_key in report_data.keys():
            report = report_data[router_reports_key]
            for len_key in report.keys():
                if len_key in data.keys():
                    data[len_key].append(report[len_key])
                else:
                    data[len_key] = [report[len_key]]
        max_len = 0
        for key in data.keys():
            if len(data[key]) > max_len:
                max_len = len(data[key])
        for key in data.keys():
            while len(data[key]) < max_len:
                data[key].append(0)
        data = dict(sorted(data.items()))
        try:

            # Set the figure size
            plt.rcParams["figure.figsize"] = [7.50, 3.50]
            plt.rcParams["figure.autolayout"] = True
            # Pandas dataframe
            pd_data = pd.DataFrame(data)
            # print(pd_data)
            # Plot the dataframe
            ax = pd_data[list(pd_data.keys())].plot(kind='box', title='boxplot')
            # Display the plot
            # plt.show()
            plt.savefig('%s%s.svg' % (graph_path, graph_name), dpi='figure', format='svg')

        except Exception as e:
            print(e)
            traceback.print_exc()

    @staticmethod
    def is_out_of_border_sqr(i: int, j: int, n_cells_sqrt: int) -> bool:
        out_of_border: bool = False
        if i > n_cells_sqrt - 1 or j > n_cells_sqrt - 1 or i < 0 or j < 0:
            out_of_border = True
        return out_of_border

    # TODO depois podemos colocar mais tipos de calculos de distancias em um ENUM caso necessario, mas acho que não sera
    @staticmethod
    def get_edges_distances(arch_type: ArchType, edges: list[list], n2c: list[list]) -> tuple[dict, list]:
        dic_edges_dist: dict = {}
        list_edges_dist: list = []
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            a: list = n2c[n1]
            b: list = n2c[n2]
            edge_distance : int =  Util.calc_dist(a,b,arch_type)
            dic_edges_dist['%d_%d' % (n1, n2)] = edge_distance
            list_edges_dist.append(edge_distance)
        return dic_edges_dist, list_edges_dist


    @staticmethod 
    def calc_dist(a:list[int],b:list[int],arch_type:ArchType):
        if arch_type == ArchType.MESH:
            return Util.dist_manhattan(a,b)
        elif arch_type == ArchType.ONE_HOP:
            return Util.dist_one_hop(a,b)
        
    @staticmethod
    def dist_manhattan(a: list[int], b: list[int]) -> int:
        ia, ja = a
        ib, jb = b
        edge_distance: int = abs(ia - ib) + abs(ja - jb)
        return edge_distance

    @staticmethod
    def dist_one_hop(a: list[int], b: list[int]) -> int:
        ia, ja = a
        ib, jb = b
        i: int = abs(ia - ib)
        j: int = abs(ja - jb)
        edge_distance: int = ceil(i / 2) + ceil(j / 2)
        return edge_distance

    @staticmethod
    def get_db_statistics(dot_file: str, dot_name: str) -> dict:
        per_graph = PeRGraph(dot_file, dot_name)

        stat: dict = {
            'name': dot_name,
            'nodes': per_graph.n_nodes,
            'edges': per_graph.n_edges,
            'ideal_cost': per_graph.n_edges,
            'max_degree': 0,
            'avg_degree': 0,
            'g_hub': {},
            'top_k_hub': [],
            'percent_multicast': 0,
            'hist_degree': {}
        }

        max_degree = 0
        avg_degree = 0
        hub_sum = 0
        for node in per_graph.nodes:
            # finding the degrees of each node and calculating the average degree for the graph
            degree = per_graph.g.degree[node]
            if degree > max_degree:
                max_degree = degree
            avg_degree += degree

            if degree > 4:
                print(per_graph.dot_name, node, degree)

            # creating the degree histogram
            if degree in stat['hist_degree'].keys():
                stat['hist_degree'][degree] += 1
            else:
                stat['hist_degree'][degree] = 1

            # finding the hub for the graph
            n_childs = len(list(per_graph.g._succ[node].keys()))
            if n_childs > 2:
                stat['g_hub'][node] = n_childs
                hub_sum += 1

        avg_degree /= per_graph.n_nodes
        stat['max_degree'] = max_degree
        stat['avg_degree'] = avg_degree
        stat['percent_multicast'] = hub_sum / per_graph.n_nodes
        stat['hist_degree'] = dict(sorted(stat['hist_degree'].items()))

        top_k_hub = sorted(stat['g_hub'].items(),
                           key=lambda item: item[1], reverse=True)
        k = ceil(len(top_k_hub) * 0.2)
        for i in range(k):
            stat['top_k_hub'] = top_k_hub[i]

        '''wr_str = ''
        for k in stats[0].keys():
            wr_str += k + ';'
        wr_str = wr_str[:-1] + '\n'
        for i in range(len(stats)):
            wr_str += '%s; ' % stats[i]['name']
            # wr_str += '%s; ' % stats[i]['bench']
            wr_str += '%d; ' % stats[i]['nodes']
            wr_str += '%d; ' % stats[i]['edges']
            wr_str += '%d; ' % stats[i]['ideal_cost']
            wr_str += '%d; ' % stats[i]['max_degree']
            wr_str += '%0.3f; ' % stats[i]['avg_degree']
            wr_str += '%s; ' % str(stats[i]['g_hub'])
            wr_str += '%s; ' % str(stats[i]['top_k_hub'])
            wr_str += '%0.3f; ' % stats[i]['percent_multicast']
            wr_str += '%s \n' % stats[i]['hist_degree']
        wr = open(_dest_dir + 'db_stats.csv', 'w')
        wr.write(wr_str)
        wr.close()
    
        # FIXME
        for j in range(len(stats)):
            wr_str = ''
            for i in range(len(stats[j]['hist_degree'])):
                wr_str += '%d;%d\n' % (i, stats[j]['hist_degree'][str(i)])
            wr = open(_dest_dir + '%s_hist.csv' % stats[j]['name'], 'w')
            wr.write(wr_str)
            wr.close()'''
        return stat


    @staticmethod
    def get_graph_annotations(edges: list[list], cycle: list[list]) -> dict:
        dic_cycle: dict = {}
        # Initialization dictionary
        for i in range(len(edges)):
            key: str = Util.func_key(edges[i][0], edges[i][1])
            dic_cycle[key]: list = []
            # print(EDGES[i])

        # print("CYCLE")
        for i in range(len(cycle)):
            found_start: bool = False
            count: int = 0
            value1: str = ''
            elem_cycle_begin: str = cycle[i][0]
            elem_cycle_end: str = cycle[i][1]

            # print(elem_cycle_begin, elem_cycle_end)
            walk_key: list = []
            for j in range(len(edges) - 1, -1, -1):

                if elem_cycle_begin == edges[j][1] and not found_start:
                    value1 = edges[j][0]
                    # print("OPAAA value1 = %s " %(value1))
                    key: str = Util.func_key(value1, elem_cycle_begin)
                    walk_key.insert(0, key)
                    dic_cycle[key].append([elem_cycle_end, count])
                    count += 1
                    found_start = True

                elif found_start and (value1 == edges[j][1] or elem_cycle_end == edges[j][0]):

                    value1, value2 = edges[j][0], edges[j][1]

                    key: str = Util.func_key(value1, value2)

                    if value1 != elem_cycle_end and value2 != elem_cycle_end:
                        walk_key.insert(0, key)
                        # dic_CYCLE[key][elem_cycle_end] = count
                        dic_cycle[key].append([elem_cycle_end, count])
                        count += 1
                    else:
                        found_start = False
                        # Go back and update values
                        # print(dic_CYCLE)
                        for k in range(0, count // 2):
                            dic_actual = dic_cycle[walk_key[k]]
                            for l in range(len(dic_actual)):
                                if dic_actual[l][0] == elem_cycle_end:
                                    dic_cycle[walk_key[k]][l][1] = k + 1
                        break  # to the next on the vector CYCLE

        return dic_cycle

    @staticmethod
    def func_key(val1, val2):
        return str(val1) + " " + str(val2)

    @staticmethod
    def func_unkey(string):
        return string.split(" ")
