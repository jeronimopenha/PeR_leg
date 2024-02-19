from src.stat_scripts.graph_exporter.graph_exporter import GraphExporter
from src.util.util import Util
import pygraphviz as pgv
from random import choice
def generate_out_vertexes(vertexes,edges):
    out_vertexes = {}
    for vertex in vertexes:
         out_vertexes[vertex] = []
    for (src,dst) in edges:
        out_vertexes[src].append(dst)
    return out_vertexes

def generate_in_vertexes(vertexes,edges):
    in_vertexes = {}
    for vertex in vertexes:
         in_vertexes[vertex] = []
    for (src,dst) in edges:
        in_vertexes[dst].append(src)
    return in_vertexes

def generate_dot_graphs_min_cost_eq_1(path_dot_files:str, output_path):
    dot_files = Util.get_files_list_by_extension(path_dot_files, ".dot")
    for dot_file,filename in dot_files:
        finished = False
        G = pgv.AGraph(dot_file)
        vertexes = list(G.nodes())
        edges = list(G.edges())
        out_vertexes = generate_out_vertexes(vertexes,edges)
        in_vertexes = generate_in_vertexes(vertexes,edges)
        while not finished:
            vertex1 = choice(vertexes)
            if len(out_vertexes[vertex1]) == 0 or (len(out_vertexes[vertex1]) + len(in_vertexes[vertex1]) == 4) :
                continue
            vertex2 = choice(out_vertexes[vertex1])
            if len(out_vertexes[vertex2]) == 0:
                continue
            vertex3 = choice(out_vertexes[vertex2])
            if (len(out_vertexes[vertex3]) + len(in_vertexes[vertex3]) == 4):
                continue
            edges.append((vertex1,vertex3))
            finished =  True
        filename += ' - MC = 1'
        GraphExporter.export_dot_graph(vertexes,edges,output_path,filename)
base=Util.get_project_root() 
generate_dot_graphs_min_cost_eq_1(base+ f'/dot_db/graphs0_dag/',base+'/dot_db/graphs1_dag/')
generate_dot_graphs_min_cost_eq_1(base+ f'/dot_db/graphs0_tree/',base+'/dot_db/graphs1_tree/')