import json
import os
import time
from src.old.python import Util

root_path: str = Util.get_project_root()
dir_json = ["yoto/yoto_pipeline/", "yott/yott_pipeline/"]
dir_dots = ["yoto_dot/yoto_pipeline/", "yott_dot/yott_pipeline/"]


def run_simul_graphs():
    for i, algorithm_dir in enumerate(dir_dots):
        partial_path = root_path + '/reports/sw/' + algorithm_dir
        for t in os.listdir(partial_path):
            for arch in ['MESH', 'ONE_HOP']:
                partial_path2 = partial_path + t + '/' + arch
                dots_list = Util.get_files_list_by_extension(partial_path2, '.dot')
                for dot_path, dot_name in dots_list:
                    th_worse, worse_path = Util.calc_worse_th_by_dot_file(dot_path, dot_name)

                    out_path = dot_path.replace(algorithm_dir, dir_json[i])[:-4]

                    with open(out_path, 'r') as f:
                        json_data = json.load(f)

                    json_data['th'] = th_worse
                    json_data['path_th'] = worse_path

                    with open(out_path, 'w') as f:
                        json.dump(json_data, f, indent=4)


if __name__ == '__main__':
    start_time = time.time()
    run_simul_graphs()
    end_time = time.time()
    print("Total time: " + str(end_time - start_time))

th_worse, worse_path = Util.calc_worse_th_by_dot_file(
    # root_path + "/benchmarks/dot_simul/test_th_x.dot", "test_th_x.dot")
    # root_path + '/benchmarks/dot_simul/test_simul_40.dot', "test_simul_40.dot")
    # root_path + '/benchmarks/dot_simul/test_simul_optimal.dot', 'test_simul_optimal.dot')
    # root_path + '/benchmarks/dot_simul/arf_w1.dot', 'arf_w1.dot')
   root_path + '/benchmarks/dot_simul/test_th_01.dot', 'test_th_01.dot')
#    root_path + '/benchmarks/dot_simul/test_th_0_jer.dot', 'test_th_0_jer.dot')

print(th_worse)
print(worse_path)
