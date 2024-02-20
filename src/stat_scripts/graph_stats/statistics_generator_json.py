from src.stat_scripts.graph_stats.interface_statistics_generator import IStatisticsGenerator
import pandas
import json
import re

class StatisticsGeneratorJSON(IStatisticsGenerator):
    @staticmethod
    def generate_statistics_pandas(data_files: list[str]) -> pandas.DataFrame:
        df = pandas.DataFrame(columns=IStatisticsGenerator.columns)
        for json_file in data_files:
            with open(json_file, 'r') as file:
                json_data = json.load(file)
                best_dist = json_data["best_dist"]
                count_dists_greater_0 = 0
                for distance in json_data['th_placement_distances'].values():
                    count_dists_greater_0 += 0 if distance == 1 else 1
                num_annotation = re.findall('NA<\d>',json_file)[0]
                num_annotation = num_annotation.replace('NA<','').replace('>','')

                dict_data = IStatisticsGenerator.generate_data_dict(json_data['graph_name'].replace('.dot', ''),
                                                                    json_data['total_edges'],
                                                                    json_data['visited_edges'],
                                                                    best_dist,
                                                                    count_dists_greater_0,
                                                                    json_data['arch_type'],
                                                                    json_data['algorithm'],
                                                                    json_data['total_threads'],
                                                                    int(num_annotation)
                                                                    )
                df = df.append(dict_data, ignore_index=True)
        return df
