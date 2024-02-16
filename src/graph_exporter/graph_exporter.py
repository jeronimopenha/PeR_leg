import pygraphviz as pgv

from src.util.util import Util
class GraphExporter:
    def export_dot_graph(vertexes,edges,path,filename):
        grafo = pgv.AGraph(directed=True)
        
        grafo.add_nodes_from(vertexes)
        grafo.add_edges_from(edges)
        path_graph = path + filename + '.dot'

        grafo.write(path_graph)
        grafo.draw(path + filename +'.png', format='png', prog='dot')

