from src.python.stat_scripts.graph_exporter.graph_exporter import GraphExporter
from src.python.stat_scripts.graph_generator.graph_pruner import GraphPrune
from src.python.util.util import Util
import pygraphviz as pgv
import networkx as nx


def generate_pruned_graphs_from_dot_files(path_dot_files: str):
    dot_files = Util.get_files_list_by_extension(path_dot_files, ".dot")
    for dot_file, filename in dot_files:
        if 'Prun' not in filename:
            G = pgv.AGraph(dot_file)
            if 'Inv' in filename:
                vertexes, edges = GraphPrune.prune_leaf_nodes(list(G.nodes()), list(G.edges()))
            else:
                vertexes, edges = GraphPrune.prune_nodes_level_0(list(G.nodes()), list(G.edges()))
            filename = filename.replace('.dot', '') + ' - Prun'
            G = nx.Graph(directed=True)
            G.add_nodes_from(vertexes)
            G.add_edges_from(edges)
            if nx.is_connected(G):
                GraphExporter.export_dot_graph(vertexes, edges, path_dot_files, filename)


base = Util.get_project_root()
generate_pruned_graphs_from_dot_files(base + f'/dot_db/graphs0_dag/')
