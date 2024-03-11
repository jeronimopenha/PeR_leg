import math
from src.python.stat_scripts.graph_exporter.graph_exporter import GraphExporter
from src.python.stat_scripts.graphlets.graphlets_generator import GraphletsGenerator
from src.python.util.per_enum import ArchType
from src.python.util.util import Util

def find_min_placement(vertexes,edges,adj_list = [(0,1),(0,-1),(1,0),(-1,0)]):
    placement_n2c = {}
    placement_c2n = {}
    dim_arch = 10
    PEs = [(i,j) for i in range(dim_arch) for j in range(dim_arch)]
    fathers = {}
    for vertex in vertexes:
        fathers[vertex] = []
    for (a,b) in edges:
        fathers[b].append(a)

    for pe in PEs:
        placement_c2n[pe] = None
    mid_cel = int(math.floor(dim_arch/2))
    for vertex in vertexes:
        backtracking(len(vertexes),vertexes,edges,vertex,(mid_cel,mid_cel),adj_list,placement_c2n,placement_n2c,fathers)

def backtracking(total_vertexes,vertexes,edges,cur_vertex,pos,adj_list,placement_c2n,placement_n2c,fathers):
    global min_cost,min_placement
    if len(placement_n2c) == total_vertexes:
        _,list_edges_dist = Util.get_edges_distances(ArchType.MESH,edges,placement_n2c)
        cost  = sum(list_edges_dist) - len(list_edges_dist)
        if  cost < min_cost:
            min_cost = cost
            min_placement = placement_c2n.copy()
        return None
    if not Util.is_out_of_border_sqr(pos[0],pos[1],math.sqrt(len(placement_c2n))) and placement_c2n[pos] == None:
        for father in fathers[cur_vertex]:
            if placement_n2c.get(father) == None:
                backtracking(total_vertexes,remain_vertexes,edges,father,pos,adj_list,placement_c2n,placement_n2c,fathers)
        placement_c2n[pos] = cur_vertex
        placement_n2c[cur_vertex] = pos
        remain_vertexes = vertexes.copy()
        remain_vertexes.remove(cur_vertex)
        for adj_cel in adj_list:
            for vertex in remain_vertexes:
                if len(fathers[vertex])!=0:
                    for father in fathers[vertex]:
                        pos = placement_n2c[father]
                        new_pos = (pos[0]+adj_cel[0],pos[1]+adj_cel[1])
                        backtracking(total_vertexes,remain_vertexes,edges,vertex,new_pos,adj_list,placement_c2n,placement_n2c,fathers)
                else:
                    new_pos = (pos[0]+adj_cel[0],pos[1]+adj_cel[1])
                    backtracking(total_vertexes,remain_vertexes,edges,vertex,new_pos,adj_list,placement_c2n,placement_n2c,fathers)

            
def generate_info_graphlets(k):
    graphlets = GraphletsGenerator.generate_connected_graphlets(k)
    global min_cost 
    global min_placement 
    already_calculed = {}
    
    for graphlet in graphlets:
        min_cost = 99999
        min_placement = None


        vertexes = list(graphlet.nodes())
        edges = list(graphlet.edges())
        num_edges = len(edges)
        num_vertexes = len(vertexes)
        dim_arch = 10
        print(graphlet.nodes(),graphlet.edges())

        if already_calculed.get((num_vertexes,num_edges)) == None and num_vertexes > 1:
            print(graphlet.nodes(),graphlet.edges())
            find_min_placement(vertexes,edges)
            path = Util.get_project_root()+"/pattern_infos/"
            filename = f"V={num_vertexes}-E={num_edges}-MC={min_cost}"
            GraphExporter.export_dot_graph(vertexes,edges,path,filename)
            with open(path+filename+".txt",mode='w') as f:
                string = ""
                matrix = [[-1 for i in range(dim_arch)] for j in range(dim_arch)]
                for k,v in min_placement.items():
                    i,j = k
                    matrix[i][j] = v

                for row in matrix:
                    string += str(row)+"\n"

                f.write(string)
            print(min_cost)
            already_calculed[num_vertexes,num_edges] = True

min_cost = 99999
min_placement = None
generate_info_graphlets(5)
    
