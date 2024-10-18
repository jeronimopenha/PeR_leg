import os
from math import sqrt
from pathlib import Path
import json
from typing import List, Tuple, Dict

import pandas as pd
from matplotlib import pyplot as plt


class Util:

    @staticmethod
    def get_project_root() -> str:
        path: Path = Path(__file__).parent.parent.parent.parent
        return str(path)

    @staticmethod
    def write_json(path: str, file_name: str, data):
        path = Util.verify_path(path)
        with open(path + file_name + '.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def verify_path(path):
        if path[-1] != '/':
            path = path + '/'
        return path

    @staticmethod
    def get_files_list_by_extension(path: str, file_extension: str) -> List[Tuple[str, str]]:
        files_list_by_extension: List[Tuple[str, str]] = [
            (os.path.join(file_path, file_name), file_name)
            for file_path, _, filenames in os.walk(path)
            for file_name in filenames
            if os.path.splitext(file_name)[1] == file_extension
        ]
        return files_list_by_extension

    @staticmethod
    def read_json(file: str) -> Dict:
        with open(file) as p_file:
            content_dic = json.load(p_file)
        return content_dic

    @staticmethod
    def save_reports(per, path: str, file_name_pref: str, rpts):
        for rpt in rpts.keys():
            Util.write_json(path, f"{per.graph.dot_name}_{file_name_pref}_{rpts[rpt]['exec_id']}", rpts[rpt])
            per.write_dot(path, f"{per.graph.dot_name}_{file_name_pref}_{rpts[rpt]['exec_id']}_placed.dot",
                          rpts[rpt]['placement'],
                          rpts[rpt]['n2c'])

    @staticmethod
    def generate_pic():
        root_path = Util.get_project_root()
        pics_folder = 'reports/fpga/pics/'

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
                plt.scatter(group['total_cost'], group['longest_path_cost'], label=f'{placer} - {edges_algorithm}',
                            s=100)

            # Customize plot
            plt.title(f'Scatter Plot for {graph}')
            plt.xlabel('Total Cost')
            plt.ylabel('Longest Path Cost')
            plt.legend(title='Placer - Edges Algorithm')
            plt.grid(True)

            plt.savefig(Util.verify_path(root_path) + pics_folder + graph, format='png')
            plt.close()

    @staticmethod
    def generate_place_vpr():
        root_path = Util.get_project_root()
        place_folder = 'reports/fpga/place/'

        files = Util.get_files_list_by_extension(f"{root_path}/reports/fpga/", ".json")
        for file in files:
            data = Util.read_json(file[0])
            f_name = f"{data['dot_name']}_{data['placer']}_{data['edges_algorithm']}_{data['exec_id']}.blif"
            nodes_idx = data["nodes_idx"]
            placement = data["placement"]
            n2c = data["n2c"]
            # Definindo o tamanho da matriz (grid) da FPGA
            grid_height = grid_width = int(sqrt(len(data["placement"])))

            # Abrindo o arquivo .place para escrita
            with open(Util.verify_path(root_path) + place_folder + f_name, 'w') as place_file:
                # Cabeçalho do arquivo PLACE
                place_file.write(f"# Placement file generated from {data['dot_name']}\n")
                place_file.write(f"# FPGA grid: {grid_width}x{grid_height}\n")
                place_file.write("# Block Name\tX\tY\tSubtile\n")

                # Para cada bloco lógico (nó), escreva a posição de colocação (placement)
                for node, idx in nodes_idx.items():
                    cell = n2c[idx]
                    if placement[cell] is not None:
                        # Calculando as coordenadas X, Y com base no índice do placement
                        x = cell % grid_width
                        y = cell // grid_width
                        sub_tile = 0  # Subtile pode ser 0 se não for relevante

                        place_file.write(f"{idx}\t{x}\t{y}\t{sub_tile}\n")

    @staticmethod
    def generate_blif_vpr():
        root_path = Util.get_project_root()
        blif_folder = 'reports/fpga/blif/'

        files = Util.get_files_list_by_extension(f"{root_path}/reports/fpga/", ".json")
        for file in files:
            data = Util.read_json(file[0])
            f_name = f"{data['dot_name']}_{data['placer']}_{data['edges_algorithm']}_{data['exec_id']}.blif"
            input_nodes = data["input_nodes"]
            output_nodes = data["output_nodes"]
            placement = data["placement"]
            edges = data["edges"]

            # Abrindo o arquivo .blif para escrita
            with open(Util.verify_path(root_path) + blif_folder + f_name, 'w') as blif_file:
                # Cabeçalho do arquivo BLIF
                blif_file.write(f"# BLIF file generated from {data['dot_name']}\n")
                blif_file.write(f".model {data['dot_name']}\n")

                # Declaração das entradas e saídas
                for in_ in input_nodes:
                    blif_file.write(".input " + f" {in_} " + "\n")
                for out_ in output_nodes:
                    blif_file.write(".output " + f" {out_}" + "\n")

                # Especificação das portas lógicas (com base no grafo)
                for edge in edges:
                    src, dst = edge
                    blif_file.write(f".names {src} {dst}\n")
                    blif_file.write("1 1\n")  # Relação simples entre nós no grafo

                # Término do modelo
                blif_file.write(".end\n")
