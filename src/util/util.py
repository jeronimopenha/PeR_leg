from math import ceil
from src.util.per_enum import ArchType
import os
import pandas as pd
import json
import traceback
import random
from pathlib import Path

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class Util(object):

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
    def get_files_list_by_extension(path: str, extension: str) -> list[list]:
        dots_path_list = [[os.path.join(path, name), name] for name in os.listdir(path)]
        files_list = [file for file in dots_path_list if os.path.isfile(file[0])]
        files_list_by_extension = [arq for arq in files_list if arq[0].lower().endswith(extension)]
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
    def get_edges_distances(edges: list[list], n2c: list[list]) -> tuple[dict, list]:
        dic_edges_dist: dict = {}
        list_edges_dist: list = []
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            a: list = n2c[n1]
            b: list = n2c[n2]
            edge_distance: int = Util.dist_manhattan(a, b)
            dic_edges_dist['%d_%d' % (n1, n2)] = edge_distance
            list_edges_dist.append(edge_distance)
        return dic_edges_dist, list_edges_dist

    @staticmethod
    def dist_manhattan(a: list[int], b: list[int]) -> int:
        ia, ja = a
        ib, jb = b
        edge_distance = abs(ia - ib) + abs(ja - jb)
        return edge_distance
