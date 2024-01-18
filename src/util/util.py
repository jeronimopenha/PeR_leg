import os
import sys
import pandas as pd
import json
import traceback
import matplotlib.pyplot as plt


class Util(object):

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
    def get_distance_table(cells_sqrt: int) -> list[list]:
        distance_tale_tmp: list[list] = [[] for i in range((cells_sqrt - 1) * 2)]
        distance_tale: list[list] = []
        for i in range(cells_sqrt):
            for j in range(cells_sqrt):
                if j == i == 0:
                    continue
                d: int = i + j
                if [i, j] not in distance_tale_tmp[d - 1]:
                    distance_tale_tmp[d - 1].append([i, j])
                if [i, -j] not in distance_tale_tmp[d - 1]:
                    distance_tale_tmp[d - 1].append([i, -j])
                if [-i, -j] not in distance_tale_tmp[d - 1]:
                    distance_tale_tmp[d - 1].append([-i, -j])
                if [-i, j] not in distance_tale_tmp[d - 1]:
                    distance_tale_tmp[d - 1].append([-i, j])
        for d in range(len(distance_tale_tmp)):
            for p in distance_tale_tmp[d]:
                distance_tale.append(p)

        return distance_tale

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

    #TODO Parei aqui
    @staticmethod
    def get_router_hist_graph_from_dict(router_reports: dict):
        data: dict = {}
        for router_reports_key in router_reports.keys():
            report = router_reports[router_reports_key]
            for len_key in report.keys():
                if len_key in data.keys():
                    data[len_key].append(report[len_key])
                else:
                    data[len_key] = [report[len_key]]
        maxlen = 0
        for key in data.keys():
            if len(data[key]) > maxlen:
                maxlen = len(data[key])
        for key in data.keys():
            while len(data[key]) < maxlen:
                data[key].append(0)

        try:
            fig_path = './exp_results/boxplots/'
            fig_name = 'test_simul.svg'

            # Set the figure size
            plt.rcParams["figure.figsize"] = [7.50, 3.50]
            plt.rcParams["figure.autolayout"] = True
            # Pandas dataframe
            pd_data = pd.DataFrame(data)
            # Plot the dataframe
            ax = pd_data[list(pd_data.keys())].plot(kind='box', title='boxplot')
            # Display the plot
            # plt.show()
            plt.savefig('%s%s' % (fig_path, fig_name), dpi='figure', format='svg')

        except Exception as e:
            print(e)
            traceback.print_exc()
