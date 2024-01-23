import os
import sys

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

import src.sw.th as _th
import src.sw.st1 as _st1
import src.sw.st2 as _st2
import src.sw.st3 as _st3
import src.sw.st4 as _st4
import src.sw.sa_pipeline.st5 as _st5
import src.sw.st6 as _st6
import src.sw.st7 as _st7
import src.sw.st8 as _st8
import src.sw.st9 as _st9
import src.sw.st10 as _st10
import src.hw.sa_pipeline.util as _u


if __name__ == '__main__':
    n_threads = 6
    sa_graph = _u.SaGraph(os.getcwd() + '/../../dot_db/mac.dot_db')
    print(sa_graph.nodes)
    print(sa_graph.neighbors)

    th = _th.St1EdgesSel(sa_graph, n_threads=n_threads)
    st1 = _st1.St1(sa_graph, n_threads=n_threads)
    st2 = _st2.St2(sa_graph)
    st3 = _st3.St3(sa_graph, n_threads=n_threads)
    st4 = _st4.St4(sa_graph)
    st5 = _st5.St5(sa_graph)
    st6 = _st6.St6()
    st7 = _st7.St7()
    st8 = _st8.St9()
    st9 = _st9.St9()
    st10 = _st10.St10()

    for i in range(288 * 1000):
        th.compute()
        st1.compute(th.output, st9.output, st1.output['wb'])
        st2.compute(st1.output)
        st3.compute(st2.output, st3.output['wb'])
        st4.compute(st3.output)
        st5.execute(st4.output)
        st6.compute(st5.output)
        st7.compute(st6.output)
        st8.compute(st7.output)
        st9.compute(st8.output)
        st10.compute(st9.output)
        # print('%d %d %d %d %d %d %d %d %d %d' % (st1.output['idx'], st2.output['idx'], st3.output['idx'], st4.output['idx'],
        #      st5.output['idx'], st6.output['idx'], st7.output['idx'], st8.output['idx'], st9.output['idx'], st10.output['idx']))
