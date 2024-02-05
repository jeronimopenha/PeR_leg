# import os
# import sys

# if os.getcwd() not in sys.path:
#    sys.path.append(os.getcwd())

# import old.src.hw.sa_pipeline.sa_components as sac
# import old.src.hw.sa_pipeline.testbenches as _t
# from src.hw.sa_pipeline.util import SaGraph

# sa_graph = SaGraph('dot_db/mac.dot_db')
'''acc = _acc.SaAccelerator(sa_graph, 1)
acc.get().to_verilog(os.getcwd() + "/verilog/sa_aws_8x8_1c")
acc = _acc.SaAccelerator(sa_graph, 10)
acc.get().to_verilog(os.getcwd() + "/verilog/sa_aws_8x8_10c")
acc = _acc.SaAccelerator(sa_graph, 1)
acc.get().to_verilog(os.getcwd() + "/verilog/sa_aws_9x9_1c")
acc = _acc.SaAccelerator(sa_graph, 10)
acc.get().to_verilog(os.getcwd() + "/verilog/sa_aws_9x9_10c")
acc = _acc.SaAccelerator(sa_graph, 1)
acc.get().to_verilog(os.getcwd() + "/verilog/sa_aws_10x10_1c")
acc = _acc.SaAccelerator(sa_graph, 10)
acc.get().to_verilog(os.getcwd() + "/verilog/sa_aws_10x10_10c")
'''
# sa_graph.n_cells = 81
# sa_graph.n_cells_sqrt = 9
# sa_comp = sac.SAComponents(sa_graph=sa_graph, n_threads=6, n_neighbors=4)
# sa_comp.create_st4_lcf().to_verilog('st4.v')
# test_bench = _t.create_sa_single_test_bench(sa_comp)

from multiprocessing import Pool, TimeoutError
import time
import os


def f(x):
    return x * x


if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # print same numbers in arbitrary order
        a = pool.imap_unordered(f, range(10))
        for i in a:
            print(i)

        # evaluate "f(20)" asynchronously
        res = pool.apply_async(f, (20,))  # runs in *only* one process
        print(res.get(timeout=1))  # prints "400"

        # evaluate "os.getpid()" asynchronously
        res = pool.apply_async(os.getpid, ())  # runs in *only* one process
        print(res.get(timeout=1))  # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        # make a single worker sleep for 10 seconds
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")
