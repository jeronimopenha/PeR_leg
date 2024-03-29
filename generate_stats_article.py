import json
from src.python.util.util import Util
import pygraphviz as pgv



def calc_in_out_vertexes_by_dot_files(path_dot_files):
    results = []
    dot_files = Util.get_files_list_by_extension(path_dot_files, ".dot")
    for dot_file,filename in dot_files:
        G = pgv.AGraph(dot_file)
        num_ins = num_outs = 0
        vertexes = list(G.nodes())
        edges = list(G.edges())
        in_vertexes = Util.generate_in_vertexes(vertexes,edges)
        out_vertexes = Util.generate_out_vertexes(vertexes,edges)
        for value in in_vertexes.values():
            if len(value) == 0:
                num_ins += 1
        for value in out_vertexes.values():
            if len(value) == 0:
                num_outs += 1
        results.append([filename, num_ins, num_outs, len(vertexes),len(edges)])
    return results

def gen_table_overleaf(path_dot_files):
    string = r'\textbf{Bench} & \textbf{In} & \textbf{Out} & \textbf{Vertex} & \textbf{Edges} & \textbf{Unvisit}\ \hline' + "\n"
    results = calc_in_out_vertexes_by_dot_files(path_dot_files)
    for result in results:
        path= Util.get_project_root()+f'/reports/sw_copy/yoto/yoto_pipeline/t_600/MESH/{result[0].replace(".dot","")}-NA<0>M<default=-1>.dot.json'
        with open(path,'r') as f:
            data = json.load(f)
        unvisited = result[4] - data['visited_edges'] 
        result.append(unvisited)
        for filename, in_v,out_v,n_vertex,n_edges,n_unvisited in [result]:
            string += f'{filename.replace(".dot","")} & {in_v} & {out_v}  & {n_vertex} & {n_edges} & {n_unvisited} \\\\' + '\n'
    
    string += r'\hline' + "\n"
    return string
base = Util.get_project_root()
# calc_in_out_vertexes_by_dot_files(base + '/benchmarks/')
print(gen_table_overleaf(base+'/benchmarks/'))