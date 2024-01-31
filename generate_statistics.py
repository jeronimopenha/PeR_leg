from src.graph_stats.statistics_generator_json import StatisticsGeneratorJSON
from src.util.util import Util

data_files = Util.get_files_list_by_extension(Util.get_project_root() + "/reports/sw/", ".json")
statistics_generator = StatisticsGeneratorJSON
new_data_files = []
for data_file in data_files:
    new_data_files.append(data_file[0])
df = statistics_generator.generate_statistics_pandas(new_data_files)
StatisticsGeneratorJSON.write_df_to_csv(df, Util.get_project_root() + "/reports/sw/", 'statistics_sw.csv')
