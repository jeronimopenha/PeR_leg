# import os
# import sys

# if os.getcwd() not in sys.path:
#    sys.path.append(os.getcwd())

# import old.src.hw.sa_pipeline.sa_components as sac
# import old.src.hw.sa_pipeline.testbenches as _t
# from src.hw.sa_pipeline.util import SaGraph

# sa_graph = SaGraph('dot_db/mac.dot_db')
'''acc = _acc.SaAccelerator(sa_graph, 1)
acc.get().to_verilog(os.getcwd() + "/verilog/sa_aws_8x8_1c")
acc = _acc.SaAccelerator(sa_graph, 10)
acc.get().to_verilog(os.getcwd() + "/verilog/sa_aws_8x8_10c")
acc = _acc.SaAccelerator(sa_graph, 1)
acc.get().to_verilog(os.getcwd() + "/verilog/sa_aws_9x9_1c")
acc = _acc.SaAccelerator(sa_graph, 10)
acc.get().to_verilog(os.getcwd() + "/verilog/sa_aws_9x9_10c")
acc = _acc.SaAccelerator(sa_graph, 1)
acc.get().to_verilog(os.getcwd() + "/verilog/sa_aws_10x10_1c")
acc = _acc.SaAccelerator(sa_graph, 10)
acc.get().to_verilog(os.getcwd() + "/verilog/sa_aws_10x10_10c")
'''
# sa_graph.n_cells = 81
# sa_graph.n_cells_sqrt = 9
# sa_comp = sac.SAComponents(sa_graph=sa_graph, n_threads=6, n_neighbors=4)
# sa_comp.create_st4_lcf().to_verilog('st4.v')
# test_bench = _t.create_sa_single_test_bench(sa_comp)
import time
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=20) as executor:
    future1 = executor.submit(time.sleep, 2)
    future2 = executor.submit(time.sleep, 10)
    print(future1.result())
    print(future2.result())
