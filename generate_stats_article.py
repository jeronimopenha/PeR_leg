from src.util.util import Util
import pygraphviz as pgv

def calc_in_out_vertexes_by_dot_files(path_dot_files):
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
        print(f'{filename} - In = {num_ins} - Out = {num_outs} - Num Vertexes = {len(vertexes)} - Num Edges = {len(edges)}')
        input()
base = Util.get_project_root()
calc_in_out_vertexes_by_dot_files(base + '/dot_db/connected/')