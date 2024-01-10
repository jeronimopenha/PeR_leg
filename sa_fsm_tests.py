import os
import sys

base_path = os.getcwd()
if base_path not in sys.path:
    sys.path.append(os.getcwd())

from src.util.proj_graph import ProjGraph
import src.hw.sa_fsm.testbenches as _t

proj_graph = ProjGraph(base_path + '/dot_db/mac.dot_db')
test_bench = _t.create_sa_single_test_bench(base_path, proj_graph)
