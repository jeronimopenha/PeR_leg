import random
from src.graph_generator.graph_generator import GraphGenerator
import pygraphviz as pgv

from src.util.util import Util


graph_generator =  GraphGenerator
dim_archs = [i for i in range(4,20+1)]
for dim_arch in dim_archs:
    print(f'dim arch {dim_arch} - qtd_pe {dim_arch*dim_arch}')
    min_len_vertex = dim_arch*(dim_arch - 1) + 1
    max_len_vertex = dim_arch*dim_arch
    num_vertexes = random.randint(min_len_vertex,max_len_vertex)
    vertexes, edges_dfg, placement_c2n = graph_generator.generate_random_graph(num_vertexes,[(0,1),(0,-1),(1,0),(-1,0)])
    # matrix = [[-1 for i in range(dim_arch)] for j in range(dim_arch)]
    # for k,v in placement_c2n.items():
    #     i,j = k
    #     matrix[i][j] = v
    # print(vertexes, edges_dfg)
    # for row in matrix:
    #     print(row)

    # Criar um grafo direcionado
    grafo = pgv.AGraph(directed=True)
    for vertex in vertexes:
        grafo.add_nodes_from(vertexes)
    # Adicionar arestas ao grafo

    grafo.add_edges_from(edges_dfg)

    # Salvar o grafo em um arquivo .dot
    grafo.write(Util.get_project_root() + f'/dot_db/graphs0/{num_vertexes}-{dim_arch}x{dim_arch}.dot')
