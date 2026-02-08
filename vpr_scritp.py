from src.py.graph.graph import Graph
from src.py.util.util import Util

root_path = Util.get_project_root()
net_folder = 'reports/fpga/net/'
place_folder = 'reports/fpga/place/'

files = Util.get_files_list_by_extension(f"{root_path}/reports/fpga/", ".json")
for file in files:
    data = Util.read_json(file[0])
    fpga_graph = Graph(data["dot_path"], data["dot_name"])

    Util.generate_vpr_data(fpga_graph, data, Util.verify_path(root_path) + net_folder,
                           Util.verify_path(root_path) + place_folder)
