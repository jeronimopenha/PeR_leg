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
    


