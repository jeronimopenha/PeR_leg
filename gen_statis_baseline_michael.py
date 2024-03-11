<<<<<<<< HEAD:src/python/stat_scripts/gen_statis_baseline_michael.py
from src.python.stat_scripts.graph_stats.statistics_generator_dot import StatisticsGeneratorDot
from src.python.util.util import Util

data_files = Util.get_files_list_by_extension(Util.get_project_root() + "/reports/results_michael/", ".dot")
========
from src.stat_scripts.graph_stats.statistics_generator_dot import StatisticsGeneratorDot
from src.util.util import Util
base = Util.get_project_root()
data_files = Util.get_files_list_by_extension(base + "/reports/results_michael/", ".dot")
>>>>>>>> monte_carlo:gen_statis_baseline_michael.py

statistics_generator = StatisticsGeneratorDot
new_data_files = []
for data_file in data_files:
    new_data_files.append(data_file[0])

df = statistics_generator.generate_statistics_pandas(new_data_files,base+'/reports/results_michael/result_iters.json')

<<<<<<<< HEAD:src/python/stat_scripts/gen_statis_baseline_michael.py
statistics_generator.write_df_to_csv(df, Util.get_project_root() + "/reports/results_michael/",
                                     'statistics_base_michael.csv')
========
statistics_generator.write_df_to_csv(df, base + "/reports/results_michael/", 'statistics_base_michael.csv')
>>>>>>>> monte_carlo:gen_statis_baseline_michael.py
