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
    for file in files:
        g = GraphFGA(file[0], file[1][:-4])
        per = FPGAPeR(g)

        algs = [EdgesAlgEnum.DEPTH_FIRST_NO_PRIORITY, EdgesAlgEnum.ZIG_ZAG_NO_PRIORITY]
        n_exec = 10
        base_folder = 'reports/fpga/'
        placers = ['yoto', 'sa']
        pre_placed_in_out = [False, True]

        for placer in placers:
            if placer == 'yoto':
                for alg in algs:
                    for pre in pre_placed_in_out:
                        reports = per.per_yoto(n_exec, alg, pre)
                        file_name_prefix = f"yoto_{alg}"
                        save_reports(per, Util.verify_path(root_path) + base_folder, file_name_prefix, reports)
            elif placer == 'yott':
                pass
            elif placer == 'sa':
                pass
