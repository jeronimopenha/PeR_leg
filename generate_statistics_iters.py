from src.stat_scripts.graph_stats.statistics_generator_dot import StatisticsGeneratorDot
from src.util.util import Util
base = Util.get_project_root()
data_files = Util.get_files_list_by_extension(base + "/results_sa_iter/", ".dot")

statistics_generator = StatisticsGeneratorDot
new_data_files = []
for data_file in data_files:
    new_data_files.append(data_file[0])

df = statistics_generator.generate_statistics_iter(new_data_files)

