import math
from src.python.stat_scripts.graph_exporter.graph_exporter import GraphExporter
from src.python.stat_scripts.graph_generator.graph_generator import GraphGenerator
import networkx as nx
from src.python.util.util import Util


def generate_connected_dags_by_num_vertexes(num_vertexes: list):
    graph_generator = GraphGenerator
    for num_vertex in num_vertexes:
        qtd_pe = int(math.pow(math.ceil(math.sqrt(num_vertex)), 2))
        dim_arch = int(math.sqrt(qtd_pe))
        print(f'Num Vertexes = {num_vertex} - qtd_pe {qtd_pe}')
        connected = False
        while not connected:
            vertexes, edges_dfg, placement_c2n = graph_generator.generate_random_dag_graph(num_vertex,
                                                                                           [(0, 1), (0, -1), (1, 0),
                                                                                            (-1, 0)])
            G = nx.Graph(directed=True)
            G.add_nodes_from(vertexes)
            G.add_edges_from(edges_dfg)
            connected = nx.is_connected(G)
        # matrix = [[-1 for i in range(dim_arch)] for j in range(dim_arch)]
        # for k,v in placement_c2n.items():
        #     i,j = k
        #     matrix[i][j] = v
        # print(vertexes, edges_dfg)
        # for row in matrix:
        #     print(row)

        path = Util.get_project_root() + f'/dot_db/graphs0_dag/'
        filename = f'dag {num_vertex} - {dim_arch}x{dim_arch}'

        GraphExporter.export_dot_graph(vertexes, edges_dfg, path, filename)


generate_connected_dags_by_num_vertexes([i for i in range(10, 401, 10)])
