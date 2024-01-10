import os
import sys

base_path = os.getcwd()
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from src.simul.yott_pipeline.yott_pipeline import YottPipeline
from src.util.proj_graph import ProjGraph

dot_file = base_path = os.getcwd() + '/dot_db/mac.dot'
proj_graph = ProjGraph(dot_file)
yott = YottPipeline(proj_graph)
yott.run()
