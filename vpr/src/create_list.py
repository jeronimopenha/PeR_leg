import sys, os.path
import networkx as nx

from module.create_index import get_index 

MAX_VALUE = -1

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
        #print("%s" % (MAX_VALUE), end = " ")
        arq.write("%s " % (MAX_VALUE))
    else: # count >= 1 
        #print( "%s" %string, end = " ")
        arq.write("%s " %string)

if __name__ == "__main__":
    
    if len(sys.argv) > 2:
        path = sys.argv[1]
        dot = sys.argv[2]
    else:
        print("python3 create_list.py <.place> <.dot>\n")
        exit(0)

    if os.path.exists(path):
        arq = open(path, "r")
    else:
        print("FILE %s not create!" %(path))
        exit(1)

    graph = nx.DiGraph(nx.drawing.nx_pydot.read_dot(dot))
    name = dot.replace("dot_", "").split("/")[-1].split(".")[0]

    dict_id, _ = get_index(graph)

    arq = open(path, "r")
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
            lista.append((int(line[1]),int(line[2]),line[0],line[4][1:]))
            if int(line[1]) > maior_x:
                maior_x = int(line[1])
            if int(line[2]) > maior_y:
                maior_y = int(line[2])
    arq.close()

    dict_lista = {}
    for i in lista:
        dict_lista[i[2]] = (i[0],i[1],i[3])

    arq = open("data/grid/"+name+".grid", "a")
    arq.write(str(size+2)+"\n")
    for i in range(size+2):
        for j in range(size+2):
            igual(i, j, lista, dict_id, arq)
    arq.write("\n")
    arq.close()