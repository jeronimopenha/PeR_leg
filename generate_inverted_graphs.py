from src.stat_scripts.graph_exporter.graph_exporter import GraphExporter
from src.stat_scripts.graph_generator.graph_inverter import GraphInverter
from src.util.util import Util
import pygraphviz as pgv

def generate_inverted_graphs_from_dot_files(path_dot_files:str):
    dot_files = Util.get_files_list_by_extension(path_dot_files, ".dot")
    for dot_file,filename in dot_files:
        if 'Inv' not in filename:
            G = pgv.AGraph(dot_file)
            inverted_edges = GraphInverter.invert_graph(G.edges())
            filename = filename.replace('.dot','') + ' - Inv'
            GraphExporter.export_dot_graph(G.nodes(),inverted_edges,path_dot_files,filename)
base=Util.get_project_root() 
generate_inverted_graphs_from_dot_files(base+ f'/dot_db/graphs0_dag/')
# generate_inverted_graphs_from_dot_files(base+ f'/dot_db/graphs0_tree/')