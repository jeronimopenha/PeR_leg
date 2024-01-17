import os 
import sys
import os
import math
# Adicionar o caminho da pasta raiz ao sys.path
sys.path.insert(0,"/home/fabio/Mestrado/PeR/")

from src.sw.yott_pipeline.stage1_yott import Stage1YOTT
from src.sw.yott_pipeline.stage2_yott import Stage2YOTT
from src.sw.yott_pipeline.stage3_yott import Stage3YOTT
from src.sw.yott_pipeline.stage4_yott import Stage4YOTT
from queue import Queue

class YOTTPipeline:
    def __init__(self,ITL: list,annotations,num_threads: int = 6):
        self.len_pipeline = 6
        self.num_threads = num_threads
        self.stage1 = Stage1YOTT(ITL,annotations,num_threads,self.len_pipeline)
        self.stage2 = Stage2YOTT(num_threads,0,6)
        self.stage3 = Stage3YOTT()
        self.stage4 = Stage4YOTT(3,0,num_threads)

    def run(self):
        FIFO = Queue()
        for i in range(self.num_threads):
            FIFO.put((i,0))
        while not self.stage1.stage_finished:
            thread_index, writed = FIFO.get()
            self.stage1.compute(thread_index, writed)
            # print(self.stage1.output)
            
            self.stage2.compute(self.stage1,self.stage4)
            # print(self.stage2.output)
            # print(self.stage2.N2C)

            self.stage3.compute(self.stage2)
            # print(self.stage3.output)   

            self.stage4.compute(self.stage3,3,FIFO)
            # print(self.stage4.output_stage2)
            # print(self.stage4.C2N)
            # input()
        self.print_grid(self.stage4.C2N)
        # print(self.stage2.N2C)
        # print(self.stage4.C2N)

    def print_grid(self,C2N):
        for thread,dic in enumerate(C2N):
            matrix = [[0 for i in range(int(math.sqrt(len(dic))))]for j in range(int(math.sqrt(len(dic))))] #type:ignore
            for k,v in dic.items():
                i,j = k
                matrix[i][j] = v

            print(f'thread {thread}')
            for row in matrix:
                print(row)


if __name__ == "__main__":
    ITL = [(1,0),(2,1),(3,2),(4,3),(5,4)]
    annotations = [[-1,-1],[0,2],[0,3],[0,2],[0,1]]
    yott_pipeline = YOTTPipeline(ITL,annotations,6)
    yott_pipeline.run()