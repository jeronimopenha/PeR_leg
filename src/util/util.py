from veriloggen import *
from math import ceil, log2, sqrt
from src.util.sagraph import SaGraph
from src.hw.sa_components import SAComponents


def initialize_regs(module: Module, values=None):
    regs = []
    if values is None:
        values = {}
    flag = False
    for r in module.get_vars().items():
        if module.is_reg(r[0]):
            regs.append(r)
            if r[1].dims:
                flag = True

    if len(regs) > 0:
        if flag:
            i = module.Integer("i_initial")
        s = module.Initial()
        for r in regs:
            if values:
                if r[0] in values.keys():
                    value = values[r[0]]
                else:
                    value = 0
            else:
                value = 0
            if r[1].dims:
                genfor = For(i(0), i < r[1].dims[0], i.inc())(r[1][i](value))
                s.add(genfor)
            else:
                s.add(r[1](value))


def create_rom_files(sa_graph: SaGraph, sa_comp: SAComponents, path: str):
    sa_graph = sa_graph
    n_cells = sa_comp.n_cells
    n_cells_sqrt = sa_comp.n_cells_sqrt
    n_neighbors = sa_comp.n_neighbors
    total_cells = pow(n_cells_sqrt, 2)

    cell_bits = sa_comp.cell_bits
    node_bits = sa_comp.node_bits

    sa_graph.reset_random()

    # create the initial grid to be placed
    c_n, n_c = sa_graph.get_initial_grid()

    # some format variables
    cn_str_f = '{:0%db}' % (node_bits + 1)
    nc_str_f = '{:0%db}' % cell_bits
    n_str_f = '{:0%db}' % (node_bits + 1)

    n_w = []
    # cell to node vector
    cn_w = [cn_str_f.format(0)
            for i in range(total_cells)]
    # node to cell vector
    nc_w = [nc_str_f.format(0)
            for i in range(total_cells)]

    # Initializing the adjacency array
    for c in range(total_cells):
        n_w.append([n_str_f.format(0) for i in range(n_neighbors)])
    # Filling the adjacency array
    for k in sa_graph.neighbors.keys():
        idx = 0
        for n in sa_graph.neighbors[k]:
            n_w[k][idx] = n_str_f.format((1 << node_bits) | n)
            idx += 1

    # set the valid bit for every filled cell
    for cni in range(total_cells):
        if c_n[cni] is not None:
            cn_w[cni] = cn_str_f.format((1 << node_bits) | c_n[cni])

    for nci in range(total_cells):
        if n_c[nci] is not None:
            nc_w[nci] = nc_str_f.format(n_c[nci])

    with open(path + '_n_c.rom', 'w') as f:
        for d in nc_w:
            f.write(d)
            f.write('\n')
        f.close()
    with open(path + '_c_n.rom', 'w') as f:
        for d in cn_w:
            f.write(d)
            f.write('\n')
        f.close()

    for i in range(n_neighbors):
        with open(path + '_n%d.rom' % i, 'w') as f:
            for c in range(n_cells):
                f.write(n_w[c][i])
                f.write('\n')
            f.close()
