import math
from src.graph_stats.interface_statistics_generator import IStatisticsGenerator
import pandas 
import json
import numpy as np
class StatisticsGeneratorJSON(IStatisticsGenerator):
    @staticmethod
    def generate_statistics_pandas(data_files:list[str]) -> pandas.DataFrame:
        df = pandas.DataFrame(columns = IStatisticsGenerator.columns)
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
                dict_data = IStatisticsGenerator.generate_data_dict(json_data['graph_name'].replace('.dot',''),
                                                                    json_data['total_edges'],
                                                                    json_data['visited_edges'],
                                                                    min_distance,
                                                                    dists_greather_0,
                                                                    json_data['arch_type'],
                                                                    json_data['algorithm'],
                                                                    json_data['total_threads'],
                                                                   )
                df = df.append(dict_data,ignore_index=True)
        return df
    
    @staticmethod
    def write_df_to_csv(df:pandas.DataFrame, output_file_path:str ,output_file_name:str):
        arch_types = df['Arch Type'].unique()
        # num_archs = len(arch_types)
        algorithms = (df['Algorithm'].unique())
        # num_algorithms = len(algorithms)
        total_executions_algorithms = ([sorted(df[df['Algorithm']== algorithm]['Total Executions'].unique().tolist()) for algorithm in algorithms])

        assert (len(total_executions_algorithms )!= 0)

        num_exec_per_algorithm = len(total_executions_algorithms[0])
        final_filter = []

        initial_filter = []
        for i,algorithm in enumerate(algorithms):
            filter = df[(df['Algorithm']== algorithm)]
            for total_exec in total_executions_algorithms[i]:
                initial_filter.append(filter[filter['Total Executions'] == total_exec])

        final_filter = []
        
        for arch_type in arch_types:
            for filter in initial_filter:
                final_filter.append(filter[filter['Arch Type'] == arch_type])
      

        comum_columns = ['Bench','N Edges','Visited Edges']
        head = ",,,"
        print(final_filter)
        for i in range(num_exec_per_algorithm):
            cur_index = i
            arch_type = final_filter[i]['Arch Type'].unique().tolist()[0]
            algorithm = final_filter[i]['Algorithm'].unique().tolist()[0]
            total_execution = final_filter[i]['Total Executions'].unique().tolist()[0]

            head += f'{algorithm} - {total_execution} - {arch_type},,'
            final_filter[i] = final_filter[i].drop(['Arch Type','Algorithm','Total Executions'],axis=1)

            if i == 0:
                new_df = final_filter[i]
            else: 
                new_df = new_df.merge(final_filter[i],on=comum_columns)
            while cur_index + num_exec_per_algorithm < len(final_filter):
                arch_type = final_filter[cur_index+num_exec_per_algorithm]['Arch Type'].unique().tolist()[0]
                algorithm = final_filter[cur_index+num_exec_per_algorithm]['Algorithm'].unique().tolist()[0]
                total_execution = final_filter[cur_index+num_exec_per_algorithm]['Total Executions'].unique().tolist()[0]
                head += f'{algorithm} - {total_execution} - {arch_type},, '
                final_filter[cur_index+num_exec_per_algorithm] = final_filter[cur_index+num_exec_per_algorithm].drop(['Arch Type','Algorithm','Total Executions'],axis=1)

                new_df = new_df.merge(final_filter[cur_index+num_exec_per_algorithm],on=comum_columns)
                cur_index += num_exec_per_algorithm
            # print(new_df.columns)
            # input()
        filename = output_file_path+output_file_name
        head+='\n'
        with open(filename, 'w') as file:
            file.write(head)
        new_df.to_csv(filename,mode='a',index=False)

