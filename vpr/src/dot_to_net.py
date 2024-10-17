import sys
import networkx as nx

def create_statistic(path_dot):

    g = nx.DiGraph(nx.drawing.nx_pydot.read_dot(path_dot))

    cont_input = 0
    cont_output = 0
    cont_no = 0
    cont_edges = 0
    cont_fanout = 0

    for no in list(g.nodes()):
        cont_no += 1
        cont_edges += g.out_degree(no)
        if g.in_degree(no) == 0:
            cont_input += 1
        if g.out_degree(no) == 0:
            cont_output += 1
        cont_fanout += g.out_degree(no)
    
    print("INPUT      = %d" %(cont_input))
    print("OUTPUT     = %d" %(cont_output))
    print("NODES      = %d" %(cont_no))
    print("EDGES      = %d" %(cont_edges))
    print("FANOUT AVG = %.2f" %(cont_fanout/(cont_no-cont_output)))


def create_net(path_dot, path_destiny):

    #print(path_net)
    arq = open(path_destiny, 'w')

    g = nx.DiGraph(nx.drawing.nx_pydot.read_dot(path_dot))

    for no in list(g.nodes()):
        if g.in_degree(no) == 0:
            arq.write('.input '+no+'\n')
            arq.write('pinlist: '+no+'\n\n')
    
    for no in list(g.nodes()):
        if g.out_degree(no) == 0:
            if ("out:" not in no):
                arq.write('.output out:'+no+'\n')
            else:
                arq.write('.output '+no+'\n')
            new_node = no.replace("out:","")
            arq.write('pinlist: '+new_node+'\n\n')

    for no in list(g.nodes()):
        if g.in_degree(no) != 0 and "out:" not in no:
            arq.write('.clb '+no+'  # Only LUT used.\n')
            arq.write('pinlist:')
            #print(no)
            i = 0
            for pre in list(g.predecessors(no)):
                arq.write(' '+pre)
                i += 1
            arq.write(' open' * (4-i))
            arq.write(' '+no)
            arq.write(' open\n')

            arq.write('subblock: '+no)
            for j in range(i):
                arq.write(' '+str(j))
            arq.write(' open' * (4-i))
            arq.write(' 4 open\n\n')
             
    arq.close()
    return

if __name__ == "__main__":

    if len(sys.argv) > 2:
        path_origin = sys.argv[1]
        path_destiny = sys.argv[2]
    else:
        print("python3 create_grid <path_origin> <path_destiny>\n")
        exit(0)
    
    #create_statistic(dot)

    create_net(path_origin, path_destiny)
