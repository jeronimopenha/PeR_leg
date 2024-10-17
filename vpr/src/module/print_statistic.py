from module.create_histogram import create_histogram

def print_statistic_histogram_cost_total(vector_dic_cost, name):

    dic_mesh, dic_1hop = {}, {}
    for i in range(len(vector_dic_cost)):
        cost = [0,0]
        for edge in vector_dic_cost[i]:
            cost[0] += vector_dic_cost[i][edge][0]
            cost[1] += vector_dic_cost[i][edge][1]
        
        if cost[0] not in dic_mesh:
            dic_mesh[cost[0]] = 1
        else:
            dic_mesh[cost[0]] += 1
        
        if cost[1] not in dic_1hop:
            dic_1hop[cost[1]] = 1
        else:
            dic_1hop[cost[1]] += 1
    
    list_x, list_y = [], []
    for i in sorted(dic_mesh):
        list_x.append(i)
        list_y.append(dic_mesh[i])
    
    label_title = name + " - MESH HISTOGRAM COST TOTAL"
    label_x = "cost"
    label_y = "qtd"
    create_histogram(list_x, list_y, label_title, label_x, label_y, "imagens/" + name + "_cost_total_mesh.pdf")

    list_x, list_y = [], []
    for i in sorted(dic_1hop):
        list_x.append(i)
        list_y.append(dic_1hop[i])
    
    label_title = name + " - 1-HOP HISTOGRAM COST TOTAL"
    label_x = "cost"
    label_y = "qtd"
    create_histogram(list_x, list_y, label_title, label_x, label_y, "imagens/" + name + "_cost_total_1hop.pdf") 

'''
'''
def print_statistic_histogram_buffer(buffer, k, name, n_edge, edges):

    dict_max_buffer = {}
    min_buffer = []
    min_value = 9999 
    for i in range(len(buffer)):
        max_buffer = -1
        for j in range(0, n_edge):
            key = str(edges[2*j]) + "_" + str(edges[2*j+1])
            if max_buffer < buffer[i][key]:
                max_buffer = buffer[i][key]
        
        if max_buffer < min_value:
            min_buffer = [i]
        elif max_buffer == min_value:
            min_buffer.append(i)

        if max_buffer not in dict_max_buffer:
            dict_max_buffer[max_buffer] = 1
        else:
            dict_max_buffer[max_buffer] += 1

    if k == 0:
        label_title = name + " - MESH HISTOGRAM BUFFER WORST"
        file_save = "imagens/" + name + "_buffer_worst_mesh.pdf"
    else:
        label_title = name + " - 1-HOP HISTOGRAM BUFFER WORST"
        file_save = "imagens/" + name + "_buffer_worst_1hop.pdf"

    label_x = "cost"
    label_y = "qtd"
    list_x, list_y = [], []

    for i in sorted(dict_max_buffer):
        #print("%d,%d" %(i,dict_max_buffer[i]))
        list_x.append(i)
        list_y.append(dict_max_buffer[i])
    create_histogram(list_x, list_y, label_title, label_x, label_y, file_save) 
    return min_buffer

'''
'''
def print_statistic_histogram_worst_edges(vector_dic_cost, name):

    dic_worst_mesh, dic_worst_1hop = {}, {}
    for i in range(len(vector_dic_cost)):
        worst_mesh = worst_1hop = -1
        for edge in vector_dic_cost[i]:
            if worst_mesh < vector_dic_cost[i][edge][0]:
                worst_mesh = vector_dic_cost[i][edge][0]
            if worst_1hop < vector_dic_cost[i][edge][1]:
                worst_1hop = vector_dic_cost[i][edge][1]
        
        if worst_mesh not in dic_worst_mesh:
            dic_worst_mesh[worst_mesh] = 1
        else:
            dic_worst_mesh[worst_mesh] += 1
        
        if worst_1hop not in dic_worst_1hop:
            dic_worst_1hop[worst_1hop] = 1
        else:
            dic_worst_1hop[worst_1hop] += 1
    
    label_x = "cost"
    label_y = "qtd"
    
    label_title = name + " - MESH HISTOGRAM EDGE WORST"
    file_save = "imagens/" + name + "_edge_worst_mesh.pdf"
    
    list_x, list_y = [], []
    for i in sorted(dic_worst_mesh):
        list_x.append(i)
        list_y.append(dic_worst_mesh[i])
    create_histogram(list_x, list_y, label_title, label_x, label_y, file_save) 
    
    label_title = name + " - 1-HOP HISTOGRAM EDGE WORST"
    file_save = "imagens/" + name + "_edge_worst_1hop.pdf"
    
    list_x, list_y = [], []
    for i in sorted(dic_worst_1hop):
        list_x.append(i)
        list_y.append(dic_worst_1hop[i])
    create_histogram(list_x, list_y, label_title, label_x, label_y, file_save)