import re
import pandas

from src.graph_stats.interface_statistics_generator import IStatisticsGenerator


class StatisticsGeneratorDot(IStatisticsGenerator):
    #fixme melhorar algoritmo
    @staticmethod
    def generate_statistics_pandas(data_files:list[str]) -> pandas.DataFrame:
        df = pandas.DataFrame(columns = IStatisticsGenerator.columns)
        pattern = re.compile(".weight=(\d+)")
        for dot_file in data_files:
            distances = []
            with open(dot_file, 'r') as file:
                for row in file:
                    result = re.findall(pattern,row)
                    if len(result) > 0 :
                        distances.append(int(result[0]))
            count_dists_greater_0 = 0
            dist_total = 0
            for distance in distances:
                dist_total += distance
                count_dists_greater_0 += 0 if distance == 0 else 1
            paths = dot_file.split("/")
            dict_data = IStatisticsGenerator.generate_data_dict( paths[-1].replace('.dot',''),
                                                               -1,
                                                                -1,
                                                                dist_total,
                                                                count_dists_greater_0,
                                                               paths[-3],
                                                               paths[-4],
                                                                paths[-2],
                                                                )
            df = df.append(dict_data,ignore_index=True)
        return df