from src.py.graph.graph_fpga import GraphFGA
from src.py.per.fpga.fpga_sw import FPGAPeR
from src.py.util.util import Util

root_path = Util.get_project_root()
g = GraphFGA(root_path + "/benchmarks/fpga/xor5.dot", "xor5")
per = FPGAPeR(g)
res = per.per_yoto(10)

a = 1
