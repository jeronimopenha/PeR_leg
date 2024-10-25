import networkx as nx
from src.py.graph.graph import Graph
from src.py.per.base.per import EdgesAlgEnum
from src.py.per.fpga.fpga_sw import FPGAPeR
from src.py.util.util import Util

if __name__ == '__main__':
    root_path = Util.get_project_root()
    files = Util.get_files_list_by_extension(f"{root_path}/benchmarks/fpga/bench_test/", ".dot")
    #files = Util.get_files_list_by_extension(f"{root_path}/benchmarks/fpga/dot_IWLS93/", ".dot")
    # files = [["/home/jeronimo/GIT/PeR/benchmarks/fpga/bench_test/xor5_K4.dot", "xor5_K4.dot"]]
    # files = [["/home/jeronimo/GIT/PeR/benchmarks/fpga/bench_test/z4ml_K4.dot", "z4ml_K4.dot"]]
    for file in files:
        g = Graph(file[0], file[1][:-4])
        # print(nx.is_directed_acyclic_graph(g.g)) is a DAG
        per = FPGAPeR(g)

        disconnected_components = list(nx.weakly_connected_components(g.g))

        n_exec = 1
        base_folder = 'reports/fpga/outputs/'
        placers = ['yott', ]
        yoto_algs = [
            EdgesAlgEnum.ZIG_ZAG,
            EdgesAlgEnum.DEPTH_FIRST_NO_PRIORITY,
            EdgesAlgEnum.DEPTH_FIRST_WITH_PRIORITY,
        ]

        for placer in placers:
            if placer == 'yoto':
                for alg in yoto_algs:
                    reports = per.per_yoto(n_exec, alg)
                    file_name_prefix = f"yoto_{alg}"
                    Util.save_reports(per, Util.verify_path(root_path) + base_folder, file_name_prefix, reports)

            elif placer == 'yott':
                reports = per.per_yott(n_exec)
                file_name_prefix = f"yott_{alg}"
                Util.save_reports(per, Util.verify_path(root_path) + base_folder, file_name_prefix, reports)
            elif placer == 'sa':
                reports = per.per_sa(n_exec)
                file_name_prefix = f"sa"
                Util.save_reports(per, Util.verify_path(root_path) + base_folder, file_name_prefix, reports)
    Util.generate_pic()
    # Util.generate_net_vpr()
