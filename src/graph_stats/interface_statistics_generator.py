from abc import ABC,abstractstaticmethod
import pandas
class IStatisticsGenerator(ABC):
    columns = ['Bench','N Edges', 'Visited Edges', 'Dist Total','Edges > 0', 'Arch Type', 'Algorithm', 'Total Executions']
    @abstractstaticmethod
    def generate_statistics_pandas(data_files:list[str]) -> pandas.DataFrame:
        pass

    def generate_data_dict(bench:str,n_edges:int,visited_edges:int,dist_total:int,edges_greater_0 :int,arch_type:str, algorithm:str,total_executions:int):
        return {IStatisticsGenerator.columns[0]:bench,
                IStatisticsGenerator.columns[1]:n_edges,
                IStatisticsGenerator.columns[2]:visited_edges,
                IStatisticsGenerator.columns[3]:dist_total,
                IStatisticsGenerator.columns[4]:edges_greater_0,
                IStatisticsGenerator.columns[5]:arch_type,
                IStatisticsGenerator.columns[6]:algorithm,
                IStatisticsGenerator.columns[7]:total_executions,
                }

    
# for report_file, file_name in report_files:
#     json_dict: dict = Util.read_json(report_file)
#     graph_name: str = json_dict["graph_name"]
#     n_threads: int = json_dict["n_threads"]
#     if graph_name not in exec_stats.keys():
#         exec_stats[graph_name] = {
#             'total_edges': json_dict["total_edges"],
#             'visited_edges': json_dict["visited_edges"],
#             'best_exec': {}
#         }
#     if n_threads not in exec_stats[graph_name]['best_exec'].keys():
#         exec_stats[graph_name]['best_exec'][n_threads] = {
#             'best_th': None,
#             'min_total_dist': None,
#             'edges_gt0': None
#         }
#     for th_key in json_dict['th_placement_distances'].keys():
#         for edge_key in json_dict['th_placement_distances'][th_key]:
#             dist: int = json_dict['th_placement_distances'][th_key]
#         # todo
#         # total_dist +=
#     a = 1
