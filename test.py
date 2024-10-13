from src.old.python.sw.qca.test_generate import result
from src.py.graph.graph import Graph
from src.py.per.fpga.fpga_sw import FPGAPeR
from src.py.util.util import Util

root_path = Util.get_project_root()
g = Graph(root_path + "/benchmarks/fpga/xor5.dot", "xor5")
per = FPGAPeR(g)
res = per.per_yoto(10)

a = 1
