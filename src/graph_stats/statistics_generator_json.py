import math
from src.graph_stats.interface_statistics_generator import IStatisticsGenerator
import pandas
import json
import numpy as np


class StatisticsGeneratorJSON(IStatisticsGenerator):
    @staticmethod
    def generate_statistics_pandas(data_files: list[str]) -> pandas.DataFrame:
        df = pandas.DataFrame(columns=IStatisticsGenerator.columns)
        for json_file in data_files:
            with open(json_file, 'r') as arquivo:
                json_data = json.load(arquivo)
                min_distance = math.inf
                dists_greather_0 = math.inf
                for placement_distances in json_data['th_placement_distances'].values():
                    count_dists_greater_0 = 0
                    total_distance = 0
                    for distance in placement_distances.values():
                        distance -= 1
                        total_distance += distance
                        count_dists_greater_0 += 0 if distance == 0 else 1
                    if total_distance < min_distance:
                        min_distance = total_distance
                        dists_greather_0 = count_dists_greater_0
                dict_data = IStatisticsGenerator.generate_data_dict(json_data['graph_name'].replace('.dot', ''),
                                                                    json_data['total_edges'],
                                                                    json_data['visited_edges'],
                                                                    min_distance,
                                                                    dists_greather_0,
                                                                    json_data['arch_type'],
                                                                    json_data['algorithm'],
                                                                    json_data['total_threads'],
                                                                    )
                df = df.append(dict_data, ignore_index=True)
        return df

    @staticmethod
    def write_df_to_csv(df: pandas.DataFrame, output_file_path: str, output_file_name: str):
        arch_types = df['Arch Type'].unique()
        num_archs = len(arch_types)
        algorithms = (df['Algorithm'].unique())
        num_algorithms = len(algorithms)
        total_executions_algorithms = (
        [sorted(df[df['Algorithm'] == algorithm]['Total Executions'].unique().tolist()) for algorithm in algorithms])
        assert (len(total_executions_algorithms) != 0)
        num_exec_per_algorith = len(total_executions_algorithms[0])
        final_filter = []

        initial_filter = []
        for i, algorithm in enumerate(algorithms):
            filter = df[(df['Algorithm'] == algorithm)]
            for total_exec in total_executions_algorithms[i]:
                initial_filter.append(filter[filter['Total Executions'] == total_exec])

        final_filter = []

        for arch_type in arch_types:
            for filter in initial_filter:
                final_filter.append(filter[filter['Arch Type'] == arch_type])

        updated_filters = []
        for filter in final_filter:
            arch_type = filter['Arch Type'].unique().tolist()[0]
            algorithm = filter['Algorithm'].unique().tolist()[0]
            total_execution = filter['Total Executions'].unique().tolist()[0]
            new_columns = {
                'Dist Total': f'DT - {arch_type} - {algorithm} - {total_execution}',
                'Edges > 0': f'E > 0 - {arch_type} - {algorithm}- {total_execution}'}
            filter = filter.rename(columns=new_columns)
            filter = filter.drop(['Arch Type', 'Algorithm', 'Total Executions'], axis=1)
            updated_filters.append(filter)
        # print(updated_filters)
        for i in range(num_exec_per_algorith):
            cur_index = i
            if i == 0:
                new_df = updated_filters[i]
            else:
                new_df = new_df.merge(updated_filters[i], on=['Bench', 'N Edges', 'Visited Edges'])
            while cur_index + num_exec_per_algorith < len(updated_filters):
                new_df = new_df.merge(updated_filters[cur_index + num_exec_per_algorith],
                                      on=['Bench', 'N Edges', 'Visited Edges'])
                cur_index += num_exec_per_algorith
            # print(new_df.columns)
            # input()
        print(new_df.columns)
        new_df.to_csv(output_file_path + output_file_name)
