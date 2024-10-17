import sys, time
import networkx as nx
import math
import numpy as np
from module.buffer_algorithm import buffer_minimize
from module.buffer_algorithm import create_buffer
from module.create_dot import create_new_dot
from module.read_inputs import read_results_vpr
from module.get_costs import get_costs_vpr
from module.get_tree import get_tree
from module.create_index import get_index, get_info 

'''
    Funtion main
'''
if __name__ == "__main__":
    
    if len(sys.argv) > 2:
        dot = sys.argv[1]
        result = sys.argv[2]
    else:
        print("python3 balanced_buffer <name.dot> <name_list.in> <results_place.in>\n")
        exit(0)
    
    name = result.split("/")[-1].split(".")[0]
    print(name, end=", ")

    g = nx.DiGraph(nx.drawing.nx_pydot.read_dot(dot))

    dict_breadth, dict_inv = get_index(g)

    n_node, n_edge, edges = get_info(g, dict_breadth)
    
    #print("number of nodes: ", n_node)
    #print("number of egdes: ", n_edge)
    #print("edges = ", edges)

    dim, v_results = read_results_vpr(result)
    #print(dim, v_results)

    #print_grid(v_results, GRID_SIZE, dict_inv)

    vector_dic_cost, N_STRATEGY = get_costs_vpr(v_results, n_node, dim, dict_inv, edges)

    dict_tree = get_tree(g)

    N_STRATEGY = 2
    
    #print(end=",")
    begin = time.time()
    buffer, vector_dict_tree = create_buffer(g, dict_tree, dict_breadth, vector_dic_cost, N_STRATEGY)
    end = time.time()

    vector_buffer = []
    #print("numero de sol = ", len(buffer))
    maior = 9999
    for i in range(len(buffer)):
        max_buffer = -1
        cost = 0
        for j in range(0, n_edge):
            key = str(edges[2*j]) + "_" + str(edges[2*j+1])
            cost += vector_dic_cost[i][key][N_STRATEGY] + 1
            if max_buffer < buffer[i][key]:
                max_buffer = buffer[i][key]
        vector_buffer.append(max_buffer)
        if cost < maior:
            maior = cost
    max_buffer_global = min(vector_buffer)

    print("%.5f, %d, %.2f\n" %((end-begin), max_buffer_global, maior/n_edge), end="")
