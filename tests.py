import os
import sys

base_path = os.getcwd()
if base_path not in sys.path:
    sys.path.append(os.getcwd())

from src.util.sagraph import SaGraph
import src.hw.testbenches as _t

sa_graph = SaGraph(base_path + '/dot/mac.dot')
test_bench = _t.create_sa_single_test_bench(base_path, sa_graph)
