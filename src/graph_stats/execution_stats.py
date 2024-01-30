from src.util.util import Util

root_path = Util.get_project_root()
base_path = root_path + "/results/sw/"
report_files = Util.get_files_list_by_extension(base_path, '.json')
graph_name: list = []
graph_total_edges: list = []
graph_visited_edges: list = []
graph_total_distance: dict = {}
graph_edges_gt0: dict = {}
a = 1
