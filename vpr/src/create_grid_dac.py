import sys, os.path
import networkx as nx
from graphviz import Source

MAX_VALUE = "-1"

table1hop = [[0,  0,  0,  1,  1,  2,  2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7],  
 [0,  1,  1,  2,  2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8],  
 [0,  1,  1,  2,  2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8],  
 [1,  2,  2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9],  
 [1,  2,  2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9],  
 [2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10],  
 [2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10],  
 [3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11],  
 [3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11],  
 [4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12],  
 [4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12],  
 [5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13],  
 [5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13],  
 [6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14],  
 [6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14],  
 [7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],  
 [7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]]

tablemesh = [[0,  0,  1,  1,  2,  2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8],  
 [0,  1,  1,  2,  2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8],  
 [1,  1,  2,  2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9],  
 [1,  2,  2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9],  
 [2,  2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10],  
 [2,  3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10],  
 [3,  3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11],  
 [3,  4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11],  
 [4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12],  
 [4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12],  
 [5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13],  
 [5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13],  
 [6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13, 14],  
 [6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14],  
 [7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15],  
 [7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],  
 [8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16]]

tablehex = [[0,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16],  
 [0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17], 
 [1,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17],  
 [2,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18],  
 [3,  3,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18],   
 [4,  4,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],  
 [5,  5,  5,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],  
 [6,  6,  6,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],  
 [7,  7,  7,  7,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],  
 [8,  8,  8,  8,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],  
 [9,  9,  9,  9,  9,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],  
 [10,10, 10, 10, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],  
 [11,11, 11, 11, 11, 11, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],  
 [12,12, 12, 12, 12, 12, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],  
 [13,13, 13, 13, 13, 13, 13, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],  
 [14,14, 14, 14, 14, 14, 14, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],  
 [15,15, 15, 15, 15, 15, 15, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]]

def create_id(g):
    
    dic_id = {}

    OPEN = []
    # get the node inputs
    cont_no = 0
    for n in g.nodes():
        cont_no += 1
        if g.in_degree(n) == 0:
            OPEN.insert(0,n)

    CLOSED = []

    count = 0
    while len(OPEN) > 0 :
        node = OPEN.pop()
        CLOSED.append(node)
        dic_id[node] = count

        for no in list(g.successors(node)):
            if no not in OPEN and no not in CLOSED:
                OPEN.insert(0, no)
        count += 1 

    #for no in dic_id:
    #    print(dic_id[no], no)

    return dic_id

def create_list_adjacent(graph):
    
    list_adjacent = []

    for no in list(graph.nodes()):
        temp = []
        temp.append(no)
        for adj in list(graph.successors(no)):
            temp.append(adj)
        list_adjacent.append(temp)
    
    return list_adjacent

def evaluate_pc(g, edge_cost):

    q = []
    for n in g.nodes():
        if g.out_degree(n) == 0:
            q.append((n,0))
    
    cp = 0
    while len(q) > 0:
        dad, cost = q.pop(0)

        son = list(g.predecessors(dad))
        for i in range(len(son)):
            child = son[i]
            if dad == child:
                continue
            key = child + '_' + dad
            new_cost = cost + edge_cost[key]

            q.append((child, new_cost))
            cp = max(new_cost, cp)
    return cp

def igual(i, j, lista, dic_id, arq):
    count = 0
    string = ""
    for value in lista:
        if (value[0], value[1]) == (i,j):
            if value[2].count("out:") >= 1 :
                break
            if count >= 1:
                string += "|"
                count += 1
            string += "%s" % dic_id[value[2]]
            #print("%" % value[3], end = "")
            count += 1
        
    if count == 0:
        pass
        #print("%s" % (MAX_VALUE), end = " ")
        #arq.write("%s " % (MAX_VALUE))
    elif count == 1:
        pass
        #print( "%s" %string, end = " ")
        #arq.write("%s " %string)
    else:
        pass
        #print(string, end = " ")
        #arq.write(string+" ")

def local_chess(pos_a_x, pos_a_y, pos_b_x, pos_b_y):

    distManhattanJ = abs(pos_a_y-pos_b_y)
    distManhattanI = abs(pos_a_x-pos_b_x)

    diff_x = abs(pos_a_x-pos_b_x)
    diff_y = abs(pos_a_y-pos_b_y)

    if diff_x + diff_y == 0:
        return 0
    else:
        if abs(pos_a_x-pos_a_y) % 2 == 0: # par
            return table1hop[distManhattanI][distManhattanJ]
        else:
            return tablemesh[distManhattanI][distManhattanJ]

def local_hex(pos_a_x, pos_a_y, pos_b_x, pos_b_y):
    
    distManhattanJ = abs(pos_a_y-pos_b_y)
    distManhattanI = abs(pos_a_x-pos_b_x)

    return tablehex[distManhattanI][distManhattanJ]

if __name__ == "__main__":
    
    if len(sys.argv) > 2:
        path = sys.argv[1]
        dot = sys.argv[2]
    else:
        print("python3 create_grid <.place> <.dot>\n")
        exit(0)

    if os.path.exists(path):
        arq = open(path, "r")
    else:
        print("FILE %s not create!" %(path))
        exit(1)

    graph = nx.DiGraph(nx.drawing.nx_pydot.read_dot(dot))
    dict_id = create_id(graph)
    
    name = dot.replace("dot_", "").split(".")[0]

    i = 0
    lista = []
    maior_x = maior_y = -1
    for line in arq:
        i += 1
        line = line.replace("\n","")

        if i == 2:
	        size = int(line.replace(" ","").split(":")[1].split("x")[0])

        if i <= 5:
            continue
        elif line != '':
            line = line.replace("\t", " ").replace("  "," ")
            line = line.split(" ")
            
            #print(line)
            lista.append((int(line[1]),int(line[2]),line[0],line[4][1:]))
            
            if int(line[1]) > maior_x:
                maior_x = int(line[1])
            if int(line[2]) > maior_y:
                maior_y = int(line[2])
    
    arq.close()
    
    list_adjacent = create_list_adjacent(graph)
    
    dict_lista = {}
    for i in lista:
        #print("%3s [%d,%d] => %s" %(i[3],i[0],i[1],i[2]))
        dict_lista[i[2]] = (i[0],i[1],i[3])
    #print()

    #arq = open("data/placement/"+name+".out", "a")
    #arq.write(str(size+2)+"\n")
    #print(size+2)
    for i in range(size+2):
        for j in range(size+2):
            igual(i,j,lista, dict_id, arq)
    #arq.write("\n")
    #print()
    arq.close()

    #print("\nPlace:\n")
    cost = 0
    cost_1hop = 0
    #cost_chess = 0
    #cost_hex = 0
    edge_mesh_cost, edge_1hop_cost = {}, {}
    for i in range(len(list_adjacent)):
        dad = list_adjacent[i][0]
        for j in range(1, len(list_adjacent[i])):
            
            son = list_adjacent[i][j]

            if dad == son:
                continue
            
            key = dad + '_' + son

            cost_local = 0
            cost_local_1hop = 0
            #cost_local_chess = 0
            #cost_local_hex = 0
            
            pos_a_x = dict_lista[dad][0]
            pos_a_y = dict_lista[dad][1]
            pos_b_x = dict_lista[son][0]
            pos_b_y = dict_lista[son][1]
            
            diff_x = abs(pos_a_x - pos_b_x)
            diff_y = abs(pos_a_y - pos_b_y)
            
            #cost_local_chess = local_chess(pos_a_x, pos_a_y, pos_b_x, pos_b_y)
            #cost_local_hex = local_hex(pos_a_x, pos_a_y, pos_b_x, pos_b_y)
            
            cost_local = max(1, diff_x + diff_y)
            cost_local_1hop = max(1, diff_x//2 + diff_x%2 + diff_y//2 + diff_y%2)

            edge_mesh_cost[key] = cost_local
            edge_1hop_cost[key] = cost_local_1hop

            #print("%3s -> %3s -> Mesh: %d Chess: %d 1-hop: %d" %(dict_lista[dad][2],dict_lista[son][2], cost_local, -1, -1))
            cost += cost_local
            cost_1hop += cost_local_1hop
            #cost_chess += cost_local_chess
            #cost_hex += cost_local_hex

    cp_mesh = evaluate_pc(graph, edge_mesh_cost)
    #cp_1hop = evaluate_pc(graph, edge_1hop_cost)

    print("cp_mesh:", cp_mesh)
    print("wire mesh: %.2f\nwire 1-hop: %.2f" %(cost/graph.number_of_edges(), cost_1hop/graph.number_of_edges()))