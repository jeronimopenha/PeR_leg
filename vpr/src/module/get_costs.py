def local_mesh(pos_a_x, pos_a_y, pos_b_x, pos_b_y):

    diff_x = abs(pos_a_x-pos_b_x)
    diff_y = abs(pos_a_y-pos_b_y)

    if diff_x + diff_y == 0:
        return 0
    else:
        return diff_x + diff_y - 1

def local_1hop(pos_a_x, pos_a_y, pos_b_x, pos_b_y):

    diff_x = abs(pos_a_x-pos_b_x)
    diff_y = abs(pos_a_y-pos_b_y)

    if diff_x + diff_y == 0:
        return 0
    else:
        return diff_x//2 + diff_y//2 + diff_x%2 + diff_y%2 - 1

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

def local_hex(pos_a_x, pos_a_y, pos_b_x, pos_b_y):

    distManhattanJ = abs(pos_a_y-pos_b_y)
    distManhattanI = abs(pos_a_x-pos_b_x)

    return tablehex[distManhattanI][distManhattanJ]

def get_costs(v_results, n_node, GRID_SIZE, dict_inv, edges):
    vector_dic_cost = []

    vector_pos = []
    for k in range(len(v_results)):
        vector_pos.append({})
    
    vector_sum_total = [[9999,-1], [9999,-1], [9999,-1], [9999,-1]] # (value, index)
    
    dict_cost_wire = []
    for k in range(4):
        dict_cost_wire.append({})

    for k in range(len(v_results)):
        positions = []
        dict_cost = {}
        for i in range(n_node):
            found = False
            for j in range(len(v_results[k])):
                if str(i) == v_results[k][j]:
                    row = j // GRID_SIZE
                    col = j % GRID_SIZE
                    positions.append((row, col))
                    found = True
                    break
            if not found:
                print("Element not found %d" %(i))
        maior_mesh, maior_1hop, maior_chess, maior_hex = 0, 0, 0, 0
        sum_total_1hop, sum_total_mesh, sum_total_chess, sum_total_hex = 0, 0, 0, 0
        for i in range(0, len(edges), 2):
            key = edges[i] + "_" + edges[i+1]
            pos_a_x = positions[int(edges[i])][0]
            pos_a_y = positions[int(edges[i])][1]
            pos_b_x = positions[int(edges[i+1])][0]
            pos_b_y = positions[int(edges[i+1])][1]

            vector_pos[k][dict_inv[edges[i]]] = [positions[int(edges[i])][0], positions[int(edges[i])][1]]
            vector_pos[k][dict_inv[edges[i+1]]] = [positions[int(edges[i+1])][0], positions[int(edges[i+1])][1]]
            
            sum_mesh_local = local_mesh(pos_a_x, pos_a_y, pos_b_x, pos_b_y)
            sum_chess_local = local_1hop(pos_a_x, pos_a_y, pos_b_x, pos_b_y)#local_chess(pos_a_x, pos_a_y, pos_b_x, pos_b_y)
            sum_1hop_local = local_1hop(pos_a_x, pos_a_y, pos_b_x, pos_b_y)
            sum_hex_local = local_1hop(pos_a_x, pos_a_y, pos_b_x, pos_b_y)#local_hex(pos_a_x, pos_a_y, pos_b_x, pos_b_y)
            
            if maior_mesh < sum_mesh_local:
                maior_mesh = sum_mesh_local
            if maior_chess < sum_chess_local:
                maior_chess = sum_chess_local
            if maior_1hop < sum_1hop_local:
                maior_1hop = sum_1hop_local
            if maior_hex < sum_hex_local:
                maior_hex = sum_hex_local
            
            sum_total_mesh += sum_mesh_local
            sum_total_chess += sum_chess_local
            sum_total_1hop += sum_1hop_local
            sum_total_hex += sum_hex_local
            #print("%2d -> %2d cost: %d" %(int(edges[i]), int(edges[i+1]), sum_1hop_local))

            dict_cost[key] = [sum_mesh_local, sum_chess_local, sum_1hop_local, sum_hex_local]
        vector_dic_cost.append(dict_cost)

        if sum_total_mesh not in dict_cost_wire[0]:
            dict_cost_wire[0][sum_total_mesh] = 1
        else:
            dict_cost_wire[0][sum_total_mesh] += 1

        if sum_total_chess not in dict_cost_wire[1]:
            dict_cost_wire[1][sum_total_chess] = 1
        else:
            dict_cost_wire[1][sum_total_chess] += 1
        
        if sum_total_1hop not in dict_cost_wire[2]:
            dict_cost_wire[2][sum_total_1hop] = 1
        else:
            dict_cost_wire[2][sum_total_1hop] += 1
        
        if sum_total_hex not in dict_cost_wire[3]:
            dict_cost_wire[3][sum_total_hex] = 1
        else:
            dict_cost_wire[3][sum_total_hex] += 1
        
        if sum_total_mesh < vector_sum_total[0][0]:
            vector_sum_total[0][0] = sum_total_mesh
            vector_sum_total[0][1] = k
        if sum_total_chess < vector_sum_total[1][0]:
            vector_sum_total[1][0] = sum_total_chess
            vector_sum_total[1][1] = k
        if sum_total_1hop < vector_sum_total[2][0]:
            vector_sum_total[2][0] = sum_total_1hop
            vector_sum_total[2][1] = k
        if sum_total_hex < vector_sum_total[3][0]:
            vector_sum_total[3][0] = sum_total_hex
            vector_sum_total[3][1] = k
        
        #print("sum = %d, index = %d" %(sum_total_mesh, k))

    return vector_dic_cost, vector_pos, vector_sum_total, dict_cost_wire

def get_costs_vpr(v_results, n_node, GRID_SIZE, dict_breadth, edges):
    vector_dic_cost = []
    positions = []
    dict_cost = {}

    dic_borders = {} 
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if i == 0 or i == GRID_SIZE-1 or j == 0 or j == GRID_SIZE-1:
                dic_borders[(i,j)] = 0

    for i in range(n_node+1):
        found = False
        for k in range(len(v_results)):
            for j in range(len(v_results[k])):
                if '|' in v_results[k][j]:
                    res = v_results[k][j].split('|')
                    for l in range(len(res)):
                        if str(i) == res[l]:
                            row = j // GRID_SIZE
                            col = j % GRID_SIZE
                            pair = (row, col)
                            if pair in dic_borders:
                                dic_borders[pair] += 1
                            positions.append(pair)
                            found = True
                            break
                    if found:
                        break
                else:
                    if str(i) == v_results[k][j]:
                        row = j // GRID_SIZE
                        col = j % GRID_SIZE
                        positions.append((row, col))
                        found = True
                        break
            if found:
                break
    
    maior_mesh, maior_1hop, maior_chess, maior_hex = 0, 0, 0, 0
    for i in range(0, len(edges), 2):
        key = edges[i] + "_" + edges[i+1]
        pos_a_x = positions[int(edges[i])][0]
        pos_a_y = positions[int(edges[i])][1]
        pos_b_x = positions[int(edges[i+1])][0]
        pos_b_y = positions[int(edges[i+1])][1]
        
        sum_local = local_mesh(pos_a_x, pos_a_y, pos_b_x, pos_b_y)
        sum_1hop_local = local_1hop(pos_a_x, pos_a_y, pos_b_x, pos_b_y)
        sum_chess_local = local_chess(pos_a_x, pos_a_y, pos_b_x, pos_b_y)
        sum_hex_local = local_hex(pos_a_x, pos_a_y, pos_b_x, pos_b_y)
        
        if maior_mesh < sum_local:
            maior_mesh = sum_local
        if maior_1hop < sum_1hop_local:
            maior_1hop = sum_1hop_local
        if maior_chess < sum_chess_local:
            maior_chess = sum_chess_local
        if maior_hex < sum_hex_local:
            maior_hex = sum_hex_local

        dict_cost[key] = [sum_local, sum_chess_local, sum_1hop_local, sum_hex_local]
    vector_dic_cost.append(dict_cost)

    return vector_dic_cost, 4