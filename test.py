from src.python.util.util import Util

vertexes = [0,1,2]
edges = [(0,1),(1,2),(0,2)]

edges_dist = {(0,1): 0, (1,2):0,(0,2):0}

print(Util.calc_worse_throughput(vertexes,edges,edges_dist))