import os
import time
from src.hw.df_simul.df_simul_hw import DfSimulHw
from src.util.per_graph import PeRGraph
from src.util.util import Util


def run_simul_graphs():
    run_parallel = False

    root_path: str = Util.get_project_root()
    dot_input = root_path + '/dot_db/dot_simul/'

    output_base = root_path + '/verilog/df_simul'

    output_folders = [output_base + '/verilog', output_base + '/results']
    for out_f in output_folders:
        if not os.path.exists(out_f):
            os.makedirs(out_f)

    # list connected benchmarks
    dots_list = Util.get_files_list_by_extension(dot_input, '.dot')

    for dot_path, dot_name in dots_list:
        print(f'DOT: {dot_name}')
        per_graph = PeRGraph(dot_path, dot_name)
        df_simul = DfSimulHw(per_graph, output_base)
        df_simul.start_simulation()


if __name__ == '__main__':
    start_time = time.time()
    run_simul_graphs()
    end_time = time.time()
    print("Total time: " + str(end_time - start_time))
