from src.sw.sa_pipeline.stage0_sa import Stage0SA
from src.sw.sa_pipeline.stage1_sa import Stage1SA
from src.sw.sa_pipeline.stage2_sa import Stage2SA
from src.sw.sa_pipeline.stage3_sa import Stage3SA
from src.sw.sa_pipeline.stage4_sa import Stage4SA
from src.sw.sa_pipeline.stage5_sa import Stage5SA
from src.sw.sa_pipeline.stage6_sa import Stage6SA
from src.sw.sa_pipeline.stage7_sa import Stage7SA
from src.sw.sa_pipeline.stage8_sa import Stage8SA
from src.sw.sa_pipeline.stage9_sa import Stage9SA
from src.sw.sa_pipeline.stage10_sa import Stage10SA
from src.util.util import Util

if __name__ == '__main__':
    n_threads = 6
    sa_graph = SaGraph(os.getcwd() + '/../../dot_db/mac.dot_db')
    print(sa_graph.nodes)
    print(sa_graph.neighbors)

    st0 = Stage0SA(sa_graph, n_threads=n_threads)
    st1 = Stage1SA(sa_graph, n_threads=n_threads)
    st2 = Stage2SA(sa_graph)
    st3 = Stage3SA(sa_graph, n_threads=n_threads)
    st4 = Stage4SA(sa_graph)
    st5 = Stage5SA(sa_graph)
    st6 = Stage6SA()
    st7 = Stage7SA()
    st8 = Stage8SA()
    st9 = Stage9SA()
    st10 = Stage10SA()

    for i in range(288 * 1000):
        st0.compute()
        st1.compute(st0.old_output, st9.old_output, st1.old_output['wb'])
        st2.compute(st1.old_output)
        st3.compute(st2.old_output, st3.old_output['wb'])
        st4.compute(st3.old_output)
        st5.compute(st4.old_output)
        st6.compute(st5.old_output)
        st7.compute(st6.old_output)
        st8.compute(st7.old_output)
        st9.compute(st8.old_output)
        st10.compute(st9.old_output)
        # print('%d %d %d %d %d %d %d %d %d %d' % (st1.output['idx'], st2.output['idx'], st3.output['idx'], st4.output['idx'],
        #      st5.output['idx'], st6.output['idx'], st7.output['idx'], st8.output['idx'], st9.output['idx'], st10.output['idx']))
