import os
import sys

base_path = os.getcwd()
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from src.sw.yolt_pipeline.yolt_pipeline_sw import YoltPipeline
from src.util.per_graph import PeRGraph

dot_file = base_path = os.getcwd() + '/dot_db/mac.dot'
# TODO automatizar a criacao das pastas
output_path = os.getcwd() + '/results/sw/yoto_pipeline/'
per_graph = PeRGraph(dot_file)
n_threads = 6
yolt = YoltPipeline(per_graph, n_threads)
results: dict = yolt.run(10)
yolt.save_results_raw(results, output_path)
