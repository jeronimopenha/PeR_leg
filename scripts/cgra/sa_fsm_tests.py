from src.old.python.util.per_graph import PeRGraph
from src.old.python import Util
import src.old.python.hw.sa_fsm.testbenches as _t

root_path: str = Util.get_project_root()
proj_graph = PeRGraph(root_path + '/dot_db/mac.dot_db')
test_bench = _t.create_sa_single_test_bench(root_path, proj_graph)
