import os
import sys

base_path = os.getcwd()
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from src.sw.yolt_pipeline.yolt_pipeline_sw import YoltPipeline
from src.util.per_graph import PeRGraph

dot_file = base_path = os.getcwd() + '/dot_db/mac.dot'
per_graph = PeRGraph(dot_file)
yolt = YoltPipeline(per_graph)
yolt.run()
