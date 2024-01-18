from src.sw.yott_pipeline.FIFOQueue import FIFOQueue
from src.sw.yott_pipeline.stage0_yott import Stage0YOTT
from src.sw.yott_pipeline.stage0_yott import Stage0YOTT
from src.sw.yott_pipeline.stage1_yott import Stage1YOTT
from src.sw.yott_pipeline.stage2_yott import Stage2YOTT
from src.sw.yott_pipeline.stage3_yott import Stage3YOTT
from src.sw.yott_pipeline.stage4_yott import Stage4YOTT
from src.sw.yott_pipeline.stage5_yott import Stage5YOTT
from src.sw.yott_pipeline.stage6_yott import Stage6YOTT

class YOTTPipeline:
    def __init__(self,ITL: list,annotations,num_threads: int = 6):
        self.len_pipeline = 7
        self.num_threads = num_threads
        self.stage0 = Stage0YOTT(FIFOQueue(num_threads))
        self.stage1 = Stage1YOTT(self.len_pipeline,annotations,len(ITL))
        self.stage2 = Stage2YOTT(ITL,annotations,num_threads)
        self.stage3 = Stage3YOTT(num_threads, self.len_pipeline,0,6)
        self.stage4 = Stage4YOTT(3)
        self.stage5 = Stage5YOTT()
        self.stage6 = Stage6YOTT(3,0,num_threads,self.len_pipeline)

    def run(self,copies: int = 1):
        for i in range(copies):
            while not self.stage0.fifo.is_empty():
                self.stage0.compute()
                # print(self.stage0.output)

                self.stage1.compute(self.stage0)
                # print(self.stage1.output)
                
                self.stage2.compute(self.stage1)
                # print(self.stage2.output)

                self.stage3.compute(self.stage2,self.stage6,9)
                # print(self.stage3.output)

                self.stage4.compute(self.stage3)
                # print(self.stage4.output)

                self.stage5.compute(self.stage4)
                # print(self.stage5.output)

                self.stage6.compute(self.stage5,self.stage0)
                # print(self.stage6.output_stage3)
                # input()
            self.print_grid(self.stage6.C2N)
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
    yott_pipeline = YOTTPipeline(ITL,annotations,4)
    yott_pipeline.run(1)