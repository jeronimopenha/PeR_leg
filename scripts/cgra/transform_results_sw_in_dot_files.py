from copy import deepcopy
import json
from src.python.util.util import Util
import networkx as nx
dir_archs = ["MESH","ONE_HOP"]
yott_ts = ["t_10","t_100","t_1000"]
yoto_ts = ["t_6","t_60","t_600"]
algorithms = [["yoto","yoto/yoto_pipeline"],["yott","yott/yott_pipeline"]] 

dir_benchs = [
    Util.get_project_root() +"/benchmarks/"
    + graphs_dir for graphs_dir in 
        ["connected/","graphs0_dag/","graphs0_tree/","graphs1_dag/","graphs1_tree/"]]

def find_dot_graph(dot_name:str,dir:str):
    dot_file_names = Util.get_files_list_by_extension(dir, ".dot")
    for complete_path, filename in dot_file_names:
          if filename == dot_name:
               return complete_path,filename
    return None
base = Util.get_project_root() +'/reports/sw/'

for algorithm_name,path_alg in algorithms:
    if algorithm_name == "yoto":
        ts = yoto_ts
    else:
        ts = yott_ts
    for t_path in ts:
        for arch_dir in dir_archs:
            complete_path = base+path_alg+"/"+t_path+"/"+arch_dir+"/"
            files = Util.get_files_list_by_extension(complete_path, ".json")
            for abs_path, filename in files:
                data = None
                with open(abs_path,'r') as f:
                    data = json.load(f)
                graph_name = data["graph_name"]
                for dir_bench in dir_benchs:
                    dfg_dot = find_dot_graph(graph_name,dir_bench)
                    if dfg_dot != None:
                        break
                assert dfg_dot != None
                G_dot = nx.drawing.nx_pydot.read_dot(dfg_dot[0])
                node_dicts = data["nodes_dict"]
                distances_dict = data["th_placement_distances"]
               
                new_digraph = nx.DiGraph()

                for (a,b,_) in G_dot.edges:
                    if distances_dict.get(f"{node_dicts[a]}_{node_dicts[b]}") != None:
                        real_dist = distances_dict[f"{node_dicts[a]}_{node_dicts[b]}"]
                    elif distances_dict.get(f"{node_dicts[b]}_{node_dicts[a]}") != None:
                        real_dist = distances_dict[f"{node_dicts[b]}_{node_dicts[a]}"]
                    else:
                        raise ValueError(f"Edge {a,b} doesn\'t exist")
                    
                    real_dist -=  1
                    assert real_dist >= 0
                    new_digraph.add_edge(a,b,weight=real_dist)
                new_path_alg = path_alg.replace(algorithm_name,f"{algorithm_name}_dot",1)
          
                with open( base+f'{new_path_alg}/{t_path}/{arch_dir}/{filename}.dot', 'w') as f:
                    f.write('digraph G {\n')
                    
                    # Escrever os vértices
                    for node in new_digraph.nodes:
                        f.write(f'    {node};\n')
                    
                    # Escrever as arestas com pesos
                    for (u,v,w) in new_digraph.edges.data():
                        w = w['weight']
                        f.write(f'    {u} -> {v} [weight={w}];\n')
                    
                    f.write('}\n')

          