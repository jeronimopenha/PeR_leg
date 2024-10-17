from src.py.graph.graph_fpga import GraphFGA
from src.py.per.base.per import EdgesAlgEnum
from src.py.per.fpga.fpga_sw import FPGAPeR
from src.py.util.util import Util


def save_reports(per: FPGAPeR, path: str, file_name_pref: str, rpts):
    for rpt in rpts.keys():
        Util.write_json(path, f"{per.graph.dot_name}_{file_name_pref}_{rpts[rpt]['exec_id']}", rpts[rpt])
        per.write_dot(path, f"{per.graph.dot_name}_{file_name_pref}_{rpts[rpt]['exec_id']}_placed.dot",
                      rpts[rpt]['placement'],
                      rpts[rpt]['n2c'])


if __name__ == '__main__':
    root_path = Util.get_project_root()
    files = Util.get_files_list_by_extension(f"{root_path}/benchmarks/fpga/dot_IWLS93/", ".dot")
    # files = [["/home/jeronimo/GIT/PeR/benchmarks/fpga/dot_IWLS93/xor5_K4.dot", "xor5_K4"]]
    for file in files:
        g = GraphFGA(file[0], file[1][:-4])
        per = FPGAPeR(g)

        n_exec = 1
        base_folder = 'reports/fpga/'
        placers = ['sa', 'yoto', ]
        yoto_algs = [EdgesAlgEnum.ZIG_ZAG_NO_PRIORITY, EdgesAlgEnum.DEPTH_FIRST_NO_PRIORITY]

        for placer in placers:
            if placer == 'yoto':
                for alg in yoto_algs:
                    if alg == EdgesAlgEnum.DEPTH_FIRST_NO_PRIORITY:
                        reports = per.per_yoto(n_exec, alg)
                        file_name_prefix = f"yoto_{alg}"
                        save_reports(per, Util.verify_path(root_path) + base_folder, file_name_prefix, reports)
                    else:
                        reports = per.per_yoto(n_exec, alg)
                        file_name_prefix = f"yoto_{alg}"
                        save_reports(per, Util.verify_path(root_path) + base_folder, file_name_prefix, reports)
            elif placer == 'yott':
                pass
            elif placer == 'sa':
                reports = per.per_sa(n_exec)
                file_name_prefix = f"sa"
                save_reports(per, Util.verify_path(root_path) + base_folder, file_name_prefix, reports)
