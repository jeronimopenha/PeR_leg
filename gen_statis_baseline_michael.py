from src.python.stat_scripts.graph_stats.statistics_generator_dot import StatisticsGeneratorDot
from src.python.util.util import Util
base = Util.get_project_root()
data_files = Util.get_files_list_by_extension(base + "/reports/results_michael/", ".dot")

statistics_generator = StatisticsGeneratorDot
new_data_files = []
for data_file in data_files:
    new_data_files.append(data_file[0])

df = statistics_generator.generate_statistics_pandas(new_data_files,base + '/reports/results_michael/result_iters.json')
print(df.Bench.unique())
# statistics_generator.write_df_to_csv(df, base + "/reports/results_michael/", 'statistics_base_michael.csv')