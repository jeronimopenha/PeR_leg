import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
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
    # files = Util.get_files_list_by_extension(f"{root_path}/benchmarks/fpga/dot_IWLS93/", ".dot")
    # files = [["/home/jeronimo/GIT/PeR/benchmarks/fpga/dot_IWLS93/xor5_K4.dot", "xor5_K4.dot"]]
    files = [["/home/jeronimo/GIT/PeR/benchmarks/fpga/dot_IWLS93/z4ml_K4.dot", "z4ml_K4.dot"]]
    for file in files:
        g = GraphFGA(file[0], file[1][:-4])
        # print(nx.is_directed_acyclic_graph(g.g)) is a DAG
        per = FPGAPeR(g)

        n_exec = 15
        base_folder = 'reports/fpga/'
        placers = ['sa', 'yoto', ]
        yoto_algs = [EdgesAlgEnum.ZIG_ZAG_WITH_PRIORITY,
                     EdgesAlgEnum.DEPTH_FIRST_WITH_PRIORITY,
                     EdgesAlgEnum.ZIG_ZAG_NO_PRIORITY,
                     EdgesAlgEnum.DEPTH_FIRST_NO_PRIORITY
                     ]

        for placer in placers:
            if placer == 'yoto':
                for alg in yoto_algs:
                    reports = per.per_yoto(n_exec, alg)
                    file_name_prefix = f"yoto_{alg}"
                    save_reports(per, Util.verify_path(root_path) + base_folder, file_name_prefix, reports)

            elif placer == 'yott':
                pass
            elif placer == 'sa':
                reports = per.per_sa(n_exec)
                file_name_prefix = f"sa"
                save_reports(per, Util.verify_path(root_path) + base_folder, file_name_prefix, reports)

    base_folder = 'reports/fpga/pics/'

    files = Util.get_files_list_by_extension(f"{root_path}/reports/fpga/", ".json")
    report = {}
    for file in files:
        rpt = Util.read_json(file[0])
        k = f"{rpt['dot_name']}_{rpt['placer']}_{rpt['edges_algorithm']}_{rpt['exec_id']}"
        if k not in report.keys():
            report[k] = {}
        report[k] = {
            'exec_id': rpt['exec_id'],
            'dot_name': rpt['dot_name'],
            'placer': rpt['placer'],
            'edges_algorithm': rpt['edges_algorithm'],
            'total_cost': rpt['total_cost'],
            'longest_path_cost': rpt['longest_path_cost']
        }

    # Step 1: Convert report dictionary into a pandas DataFrame for easier handling
    df = pd.DataFrame.from_dict(report, orient='index')

    # Step 3: Create scatter plots for each unique graph in 'dot_name'
    graphs = df['dot_name'].unique()

    for graph in graphs:
        # Filter the data for this graph
        graph_data = df[df['dot_name'] == graph]

        # Create a new figure for this graph
        plt.figure(figsize=(10, 6))

        # Group data by placer and edges_algorithm to create series, but include all exec_ids in the same series
        for (placer, edges_algorithm), group in graph_data.groupby(['placer', 'edges_algorithm']):
            # Plot multiple points for each combination of placer and edges_algorithm
            plt.scatter(group['total_cost'], group['longest_path_cost'], label=f'{placer} - {edges_algorithm}', s=100)

        # Customize plot
        plt.title(f'Scatter Plot for {graph}')
        plt.xlabel('Total Cost')
        plt.ylabel('Longest Path Cost')
        plt.legend(title='Placer - Edges Algorithm')
        plt.grid(True)

        plt.savefig(Util.verify_path(root_path) + base_folder + graph, format='png')
        plt.close()
