from src.sw.yott_pipeline.yott_pipeline_sw import YOTTPipeline
from src.util.per_enum import ArchType
from src.util.per_graph import PeRGraph
from src.util.yott.yott import YOTT


per_graph = PeRGraph("/home/fabio/Mestrado/PeR/dot_db/connected/arf.dot")
annotations = [[0,1],[0,2],[0,3],[0,2],[-1,-1],[-1,-1]]
yott_pipeline = YOTTPipeline(annotations,per_graph,ArchType.MESH,2,)
print(yott_pipeline.run(1))
