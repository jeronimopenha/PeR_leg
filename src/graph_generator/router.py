import math
import random
from src.util.util import Util


class Router:
    @staticmethod
    def create_dag_by_pe(placement_c2n: dict[int,int],
                              pe_id: int, adj_list:list[tuple[int,int]]):
        
        assert placement_c2n[pe_id] != None, "There must be a node placed in this PE"        
        
        fila = [pe_id]
        len_pes = len(placement_c2n)
        visited_pes = {pe_id:True}
        pes_alocated_in_fifo = {pe_id:True}
        father = {pe_id: None}

        routing = []
        while len(fila) > 0:
            cur_pe = fila.pop(0)
            visited_pes[cur_pe] = True
            # print(cur_pe)
            
            for neighboor in [(cur_pe[0]+a,cur_pe[1]+b) for (a,b) in adj_list]:
                if not Util.is_out_of_border_sqr(neighboor[0],neighboor[1],math.sqrt(len_pes)) :
                    if placement_c2n[neighboor] != None and visited_pes.get(neighboor) is None:
                        if father.get(neighboor) == None:
                            routing.append((cur_pe,neighboor))
                            father[neighboor] = cur_pe
                        else:
                            if random.random() <= 0.3:
                                routing.append((cur_pe,neighboor))

                        if pes_alocated_in_fifo.get(neighboor) is None:
                            fila.append(neighboor)
                            pes_alocated_in_fifo[neighboor] = True
                    
        return routing
    
    @staticmethod
    def create_tree_by_pe(placement_c2n: dict[int,int],
                              pe_id: int, adj_list:list[tuple[int,int]]):
        
        assert placement_c2n[pe_id] != None, "There must be a node placed in this PE"        
        
        fila = [pe_id]
        len_pes = len(placement_c2n)
        visited_pes = {pe_id:True}
        pes_alocated_in_fifo = {pe_id:True}
        father = {pe_id: None}

        routing = []
        while len(fila) > 0:
            cur_pe = fila.pop(0)
            visited_pes[cur_pe] = True
            
            for neighboor in [(cur_pe[0]+a,cur_pe[1]+b) for (a,b) in adj_list]:
                if not Util.is_out_of_border_sqr(neighboor[0],neighboor[1],math.sqrt(len_pes)) :
                    if placement_c2n[neighboor] != None and visited_pes.get(neighboor) is None:
                        if father.get(neighboor) == None:
                            routing.append((cur_pe,neighboor))
                            father[neighboor] = cur_pe
                        else:
                            if random.random() <= 0.5:
                                routing.append((cur_pe,neighboor))
                                routing.remove((father[neighboor],neighboor))
                                father[neighboor] = cur_pe

                        if pes_alocated_in_fifo.get(neighboor) is None:
                            fila.append(neighboor)
                            pes_alocated_in_fifo[neighboor] = True
                    
        return routing