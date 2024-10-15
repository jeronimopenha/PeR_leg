from src.py.graph.graph_fpga import GraphFGA
from src.py.per.base.per import EdgesAlgEnum
from src.py.per.fpga.fpga_sw import FPGAPeR
from src.py.util.util import Util


def save_reports(per, path, file_name_pref, rpts):
    for rpt in rpts.keys():
        Util.write_json(path, f"{file_name_pref}_{rpts[rpt]['exec_id']}", rpts[rpt])
        per.write_dot(path, f"{file_name_pref}_{rpts[rpt]['exec_id']}_placed.dot", rpts[rpt]['placement'], rpts[rpt]['n2c'])

if __name__ == '__main__':
    root_path = Util.get_project_root()
    g = GraphFGA(root_path + "/benchmarks/fpga/IWLS93_dot/xor5.dot", "xor5")
    per = FPGAPeR(g)

    algs = [EdgesAlgEnum.DEPTH_FIRST_NO_PRIORITY,EdgesAlgEnum.ZIG_ZAG_NO_PRIORITY]
    n_exec = 10
    base_folder = 'reports/fpga/'
    placers = ['yoto', 'sa']

    for placer in placers:
        if placer == 'yoto':
            for alg in algs:
                reports = per.per_yoto(n_exec, alg)
                file_name_prefix = f"yoto_{alg}"
                save_reports(per,base_folder, file_name_prefix, reports)
        elif placer == 'yott':
            pass
        elif placer == 'sa':
            pass
