from veriloggen import *
from math import ceil, log2, sqrt
from src.util.util import create_rom_files, initialize_regs
from src.util.sagraph import SaGraph
from src.hw.sa_components import SAComponents


def create_sa_single_test_bench(base_path: str, sa_graph: SaGraph, test_number: int = 0) -> str:
    # create_rom_files(comp, os.getcwd() + "/verilog")

    bus_width = 16
    sa_graph = sa_graph
    sa_comp = SAComponents(sa_graph)

    # sa_graph = comp.sa_graph
    # n_cells = comp.n_cells
    # n_neighbors = comp.n_neighbors
    # align_bits = comp.align_bits
    # n_threads = comp.n_threads

    # c_bits = ceil(log2(n_cells))
    # t_bits = ceil(log2(n_threads))
    # t_bits = 1 if t_bits == 0 else t_bits
    # node_bits = c_bits
    # lines = columns = int(sqrt(n_cells))
    # w_bits = t_bits + c_bits + node_bits + 1
    # dist_bits = c_bits + ceil(log2(n_neighbors * 2))
    # lc_bits = ceil(log2(lines)) * 2
    name = 'test_bench_sa_single_%d' % test_number
    dumpfile = base_path + "/verilog/%s.vcd" % name
    verilog_file = base_path + "/verilog/%s.v" % name
    output_file = base_path + "/verilog/a.out"

    m = Module(name)

    clk = m.Reg('clk')
    rst = m.Reg('rst')
    start = m.Reg('start')

    done = m.Wire('done')

    par = []
    con = [
        ('clk', clk),
        ('rst', rst),
        ('start', start),
        ('done', done),
    ]
    sa_single = sa_comp.create_sa_fsm_single_thread()
    m.Instance(sa_single, sa_single.name, par, con)

    initialize_regs(m, {'clk': 0, 'rst': 1, 'start': 0})

    simulation.setup_waveform(m, dumpfile=dumpfile)
    m.Initial(
        EmbeddedCode('@(posedge clk);'),
        EmbeddedCode('@(posedge clk);'),
        EmbeddedCode('@(posedge clk);'),
        rst(0),
        start(1),
        Delay(1000), Finish()
    )
    m.EmbeddedCode('always #5clk=~clk;')
    m.Always(Posedge(clk))(
        If(done)(
            Display('ACC DONE!'),
            Finish()
        )
    )
    m.EmbeddedCode('\n//Simulation sector - End')

    m.to_verilog(verilog_file)
    sim = simulation.Simulator(m, sim='iverilog')
    rslt = sim.run(outputfile=output_file)
    print(rslt)
