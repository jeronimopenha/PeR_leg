from src.graph_stats.statistics_generator_dot import StatisticsGeneratorDot
from src.util.util import Util

data_files = Util.get_files_list_by_extension(Util.get_project_root() + "/reports/results_michael/", ".dot")

statistics_generator = StatisticsGeneratorDot
new_data_files = []
for data_file in data_files:
    new_data_files.append(data_file[0])

df = statistics_generator.generate_statistics_pandas(new_data_files)

statistics_generator.write_df_to_csv(df, Util.get_project_root() + "/reports/results_michael/", 'statistics_base_michael.csv')
