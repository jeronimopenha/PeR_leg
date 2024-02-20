from src.stat_scripts.graph_exporter.graph_exporter import GraphExporter
from src.stat_scripts.graph_generator.graph_pruner import GraphPrune
from src.util.util import Util
import pygraphviz as pgv 
import networkx as nx
def generate_pruned_graphs_from_dot_files(path_dot_files:str):
    dot_files = Util.get_files_list_by_extension(path_dot_files, ".dot")
    for dot_file,filename in dot_files:
        if 'Prun' not in filename:
            G = pgv.AGraph(dot_file)
            if 'Inv' in filename:
                vertexes,edges = GraphPrune.prune_leaf_nodes(list(G.nodes()), list(G.edges()))
            else:
                vertexes,edges = GraphPrune.prune_nodes_level_0(list(G.nodes()), list(G.edges()))
            filename = filename.replace('.dot','') + ' - Prun'
            G = nx.Graph(directed=True)
            G.add_nodes_from(vertexes)
            G.add_edges_from(edges)
            if nx.is_connected(G):
                GraphExporter.export_dot_graph(vertexes,edges,path_dot_files,filename)

def prune_graph_from_dot_file(path_dotfile,dot_file,type):
    G = pgv.AGraph(path_dotfile+dot_file)
    vertexes = list(G.nodes())
    edges = list(G.edges())
    if type == 'leaf':
        vertexes,edges = GraphPrune.prune_leaf_nodes(vertexes,edges)
    elif type == 'root':
       vertexes,edges = GraphPrune.prune_nodes_level_0(vertexes,edges)
    G = nx.Graph(directed=True)

    G.add_nodes_from(vertexes)
    G.add_edges_from(edges)
    if nx.is_connected(G):
        GraphExporter.export_dot_graph(vertexes,edges,path_dotfile,dot_file.replace(".dot",''))
    
base=Util.get_project_root() 
prune_graph_from_dot_file(base+'/dot_db/graphs0_dag/',"dag 60 - 8x8.dot",'root')
# generate_pruned_graphs_from_dot_files(base+ f'/dot_db/graphs0_dag/')
