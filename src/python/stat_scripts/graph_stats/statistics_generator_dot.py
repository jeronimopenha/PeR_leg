import re
import pandas
import json
from src.python.stat_scripts.graph_stats.interface_statistics_generator import IStatisticsGenerator
from src.python.util.util import Util


class StatisticsGeneratorDot(IStatisticsGenerator):
    @staticmethod
    def generate_statistics_pandas(data_files: list[str], results_iter_json_file: str) -> pandas.DataFrame:
        df = pandas.DataFrame(columns=IStatisticsGenerator.columns)
        pattern = re.compile(".weight=(\d+)")
        for dot_file in data_files:
            edges = 0
            distances = []
            with open(dot_file, 'r') as file:
                for row in file:
                    result = re.findall(pattern, row)
                    if len(result) > 0:
                        edges += 1
                        distances.append(int(result[0]))
            count_dists_greater_0 = 0
            dist_total = 0
            for distance in distances:
                dist_total += distance
                count_dists_greater_0 += 0 if distance == 0 else 1
            dirs = dot_file.split("/")
            dot_name = dirs[-1]
            print(dot_file,dot_name)
            th_worse, worse_path = Util.calc_worse_th_by_dot_file(dot_file,dot_name)

            dict_data = IStatisticsGenerator.generate_data_dict(dot_name.replace('.dot', ''),
                                                                edges,
                                                                -1,
                                                                dist_total,
                                                                count_dists_greater_0,
                                                                dirs[-3],
                                                                dirs[-4],
                                                                dirs[-2],
                                                                0,
                                                                th_worse
                                                                )
            df.loc[len(df)] = dict_data

        with open(results_iter_json_file, 'r') as arquivo:
            js = json.load(arquivo)

        temp_df = pandas.DataFrame(columns=[IStatisticsGenerator.columns[0], 'Iters'])

        for data in js:
            graph, iters = data.values()
            graph_name = graph.replace('.dot', '')
            dict_data = {IStatisticsGenerator.columns[0]: graph_name, 'Iters': iters}
            temp_df.loc[(len(temp_df))] = dict_data

        # benchs = df['Bench'].unique().tolist()

        df = pandas.merge(df, temp_df, on=IStatisticsGenerator.columns[0])

        return df

    @staticmethod
    def generate_statistics_iter(data_files: list[str]) -> pandas.DataFrame:
        df = pandas.DataFrame(columns=['Bench', 'Dist Total', 'Edges > 0', 'Total Executions', 'Max Iter', 'Arch Type'])
        pattern = re.compile(".weight=(\d+)")
        for dot_file in data_files:
            edges = 0
            distances = []
            with open(dot_file, 'r') as file:
                for row in file:
                    result = re.findall(pattern, row)
                    if len(result) > 0:
                        edges += 1
                        distances.append(int(result[0]))
            count_dists_greater_0 = 0
            dist_total = 0
            for distance in distances:
                dist_total += distance
                count_dists_greater_0 += 0 if distance == 0 else 1

            max_iter = re.findall('MI<\d+>', dot_file)[0]
            max_iter = max_iter.replace('MI<', '').replace('>', '')
            dirs = dot_file.split("/")
            bench = ''
            for letter in dirs[-1]:
                if letter == '.':
                    break
                bench += letter
            dict_data = {'Bench': bench, 'Dist Total': dist_total, 'Edges > 0': count_dists_greater_0,
                         'Arch Type': dirs[-3], 'Total Executions': dirs[-2], 'Max Iter': max_iter}

            df.loc[len(df)] =dict_data
        return df
