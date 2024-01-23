from src.util.per_graph import PeRGraph
from src.sw.yott_pipeline.FIFOQueue import FIFOQueue
from src.sw.yott_pipeline.stage0_yott import Stage0YOTT

from src.sw.yott_pipeline.stage0_yott import Stage0YOTT
from src.sw.yott_pipeline.stage1_yott import Stage1YOTT
from src.sw.yott_pipeline.stage2_yott import Stage2YOTT
from src.sw.yott_pipeline.stage3_yott import Stage3YOTT
from src.sw.yott_pipeline.stage4_yott import Stage4YOTT
from src.sw.yott_pipeline.stage5_yott import Stage5YOTT
from src.sw.yott_pipeline.stage6_yott import Stage6YOTT
from src.util.yott.yott import YOTT

class YOTTPipeline(YOTT):
    def __init__(self,annotations,per_graph: PeRGraph,num_threads: int = 7):
        self.annotations = annotations
        super().__init__(per_graph, num_threads)
        self.ITL = self.edges_int
        #FIXME retirar
        self.annotations = [[-1,-1] for i in range(len(self.ITL))]

    def run(self,copies: int = 1):
        results: dict = {}

        for t in range(copies):
            results_key = 'exec_%d' % t
            results[results_key] = []
             
            N2C, C2N = self.get_initial_position_ij(self.edges_int[0][0], self.latency)
            
            stage0 = Stage0YOTT(FIFOQueue(self.n_threads),self.latency)
            # FIXME zigzag deve conter apenas arestas que mapeiam todos os nós
            stage1 = Stage1YOTT(self.latency,self.annotations,len(self.ITL))
            stage2 = Stage2YOTT(self.ITL,self.annotations,self.n_threads)
            stage4 = Stage4YOTT(self.per_graph.n_cells_sqrt)
            stage3 = Stage3YOTT(self.latency,N2C)
            stage5 = Stage5YOTT()
            stage6 = Stage6YOTT(self.per_graph.n_cells_sqrt,self.latency,C2N)
            len_adjacentes_indexes = len(stage4.distance_table)
            while not stage0.fifo.is_empty():
                stage0.compute()
                

                stage1.compute(stage0)
                
                
                stage2.compute(stage1)
                

                stage3.compute(stage2,stage6,len_adjacentes_indexes)
                

                stage4.compute(stage3)
                
                stage5.compute(stage4)
                
                stage6.compute(stage5,stage0)
                
                print(stage0.output)
                print(stage1.output)
                print(stage2.output)
                print(stage3.output)
                print(stage4.output)
                print(stage5.output)
                print(stage6.output_stage3)
                print()

                # input()
            self.print_grid(stage6.C2N)
            # print(self.stage2.N2C)
            # print(self.stage4.C2N)
            results[results_key].append('Total execution clocks: %d\n' % stage0.total_pipeline_counter)
            th_dict: dict = {}
            for th in range(self.latency):
                th_key = 'Time_%d_TH_%d' % (th, t)
                th_dict[th_key] = []
                th_dict[th_key].append('thread - %d, loop counter: %d' % (th, stage0.exec_counter[th]))
                th_dict[th_key].append(stage6.C2N[th])
            results[results_key].append(th_dict)
        return results

    def print_grid(self,C2N):
        for idx_thread,thread in enumerate(C2N):
            print(f'thread{idx_thread}')
            for row in thread:
                print(row)
            print()


