import os
import sys

base_path = os.getcwd()
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from src.simul.yolt_pipeline.yolt_pipeline import YoltPipeline
from src.util.proj_graph import ProjGraph

dot_file = base_path = os.getcwd() + '/dot_db/mac.dot'
proj_graph = ProjGraph(dot_file)
yolt = YoltPipeline(proj_graph)
yolt.run()
