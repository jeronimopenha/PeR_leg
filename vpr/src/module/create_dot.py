import networkx as nx
import matplotlib.pyplot as plt

def create_new_dot(g, name, dict_tree, dict_breadth, vector_dic_cost, buffer, k, min_index, vector_dict_tree):

    #new_g = nx.grid_2d_graph(5, 5)  # 5x5 grid
    path_dot = name + "_" + str(min_index) + ".dot"

    print(dict_tree)
    print(buffer[min_index])

    new_g = nx.DiGraph()
    
    OPEN = []
    label_node = {}
    # get the node inputs
    for n in g.nodes():
        if g.in_degree(n) == 0:
            OPEN.insert(0,n)
            label_node[n] = n + "[%d,%d]" %(dict_tree[n], vector_dict_tree[min_index][n])
    
    CLOSED = []
    
    while len(OPEN) > 0 :
        dad = OPEN.pop()
        CLOSED.append(dad)
        for son in list(g.successors(dad)):
            new_g.add_edge(dad,son)
            key = str(dict_breadth[dad]) + "_" + str(dict_breadth[son])
            label_node[son] = son + "[%d,%d]" %(dict_tree[son], vector_dict_tree[min_index][dad])
            if vector_dic_cost[min_index][key][k] > 0:
                new_g[dad][son]['weight'] = vector_dic_cost[min_index][key][k]
            if buffer[min_index][key] > 0:
                new_g[dad][son]['buffer'] = buffer[min_index][key]
            
            if son not in OPEN and son not in CLOSED:
                OPEN.insert(0, son)
    
    pos = nx.drawing.nx_agraph.graphviz_layout(g, prog='dot')
    arc_weight = nx.get_edge_attributes(new_g, 'weight')
    arc_buffer = nx.get_edge_attributes(new_g, 'buffer')
    
    nx.draw_networkx(new_g, pos, node_size=800, with_labels=False)
    nx.draw_networkx_labels(new_g, pos, font_size=7, labels=label_node)
    nx.draw_networkx_edge_labels(new_g, pos, edge_labels=arc_weight, rotate=False, font_color='r', font_size=7, label_pos=0.45, clip_on=False)
    nx.draw_networkx_edge_labels(new_g, pos, edge_labels=arc_buffer, rotate=False, font_color='b', font_size=7, label_pos=0.55)
    
    #nx.networkx.drawing.nx_pydot.write_dot(new_g, path_dot)
    plt.axis('off')
    # Show the plot
    plt.show()
    plt.clf() 

def create_new_dot_inverse(g, name, dict_tree, dict_breadth, vector_dic_cost, buffer, k, min_index, vector_dict_tree):

    #new_g = nx.grid_2d_graph(5, 5)  # 5x5 grid
    path_dot = name + "_" + str(min_index) + ".dot"

    #print(dict_tree)
    #print(buffer[min_index])

    new_g = nx.DiGraph()
    
    OPEN = []
    label_node = {}
    # get the node inputs
    for n in g.nodes():
        if g.out_degree(n) == 0:
            OPEN.insert(0,n)
            label_node[n] = n + "[%d,%d]" %(dict_tree[n], vector_dict_tree[min_index][n])
    
    CLOSED = []
    
    while len(OPEN) > 0 :
        son = OPEN.pop()
        CLOSED.append(son)
        for dad in list(g.predecessors(son)):
            new_g.add_edge(dad,son)
            key = str(dict_breadth[dad]) + "_" + str(dict_breadth[son])
            label_node[dad] = dad + "[%d,%d]" %(dict_tree[dad], vector_dict_tree[min_index][dad])
            if vector_dic_cost[min_index][key][k] > 0:
                new_g[dad][son]['weight'] = vector_dic_cost[min_index][key][k]
            if buffer[min_index][key] > 0:
                new_g[dad][son]['buffer'] = buffer[min_index][key]
            if dad not in OPEN and dad not in CLOSED:
                OPEN.insert(0, dad)
    
    pos = nx.drawing.nx_agraph.graphviz_layout(g, prog='dot')
    arc_weight = nx.get_edge_attributes(new_g, 'weight')
    arc_buffer = nx.get_edge_attributes(new_g, 'buffer')
    
    nx.draw_networkx(new_g, pos, node_size=800, with_labels=False, arrows=False)
    nx.draw_networkx_labels(new_g, pos, font_size=7, labels=label_node)
    nx.draw_networkx_edge_labels(new_g, pos, edge_labels=arc_weight, rotate=False, font_color='r', font_size=7, label_pos=0.4, clip_on=False)
    nx.draw_networkx_edge_labels(new_g, pos, edge_labels=arc_buffer, rotate=False, font_color='b', font_size=7, label_pos=0.6)
    
    #nx.networkx.drawing.nx_pydot.write_dot(new_g, path_dot)
    plt.axis('off')
    # Show the plot
    plt.show()
    plt.clf() 