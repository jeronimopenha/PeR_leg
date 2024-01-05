from veriloggen import *
from math import ceil, log2, sqrt


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


def create_rom_files(sa_comp, path: str):
    sa_graph = sa_comp.sa_graph
    n_cells = sa_comp.sa_graph.n_cells
    n_neighbors = sa_comp.n_neighbors
    align_bits = sa_comp.align_bits
    n_threads = sa_comp.n_threads

    c_bits = ceil(log2(n_cells))
    t_bits = ceil(log2(n_threads))
    t_bits = 1 if t_bits == 0 else t_bits
    node_bits = c_bits
    lines = columns = int(sqrt(n_cells))
    w_bits = t_bits + c_bits + node_bits + 1
    dist_bits = c_bits + ceil(log2(n_neighbors * 2))

    sa_graph.reset_random()

    c_n = []
    n_c = []
    for i in range(n_threads):
        c_n_i, n_c_i = sa_graph.get_initial_grid()
        c_n.append(c_n_i)
        n_c.append(n_c_i)

    cn_str_f = '{:0%db}' % (node_bits + 1)
    nc_str_f = '{:0%db}' % (c_bits)
    n_str_f = '{:0%db}' % (node_bits + 1)
    t_str = '{:0%db}' % (t_bits)

    cn_w = []  # [cn_str_f.format(0) for i in range(n_cells)]
    nc_w = []  # [nc_str_f.format(0) for i in range(n_cells)]
    p_w = []  # [p_str_f.format(0) for i in range(n_cells)]
    n_w = []
    for t in range(pow(2, ceil(sqrt(n_threads)))):
        cn_w.append([cn_str_f.format(0)
                     for i in range(ceil(sqrt(n_cells)) * ceil(sqrt(n_cells)))])
        nc_w.append([nc_str_f.format(0)
                     for i in range(ceil(sqrt(n_cells)) * ceil(sqrt(n_cells)))])

    for c in range(pow(2, ceil(sqrt(n_cells)))):
        n_w.append([n_str_f.format(0) for i in range(n_neighbors)])
    for k in sa_graph.neighbors.keys():
        idx = 0
        for n in sa_graph.neighbors[k]:
            n_w[k][idx] = n_str_f.format((1 << node_bits) | n)
            idx += 1

    for t in range(len(c_n)):
        for cni in range(len(c_n[t])):
            if c_n[t][cni] is not None:
                cn_w[t][cni] = cn_str_f.format((1 << node_bits) | c_n[t][cni])

    for t in range(len(n_c)):
        for nci in range(len(n_c[t])):
            if n_c[t][nci] is not None:
                nc_w[t][nci] = nc_str_f.format(n_c[t][nci])

    with open(path + '/th.rom', 'w') as f:
        for i in range(pow(2, ceil(sqrt(n_threads)))):
            f.write(t_str.format(0))
            f.write('\n')
        f.close()

    with open(path + '/n_c.rom', 'w') as f:
        for t in nc_w:
            for d in t:
                f.write(d)
                f.write('\n')
        if n_threads == 1:
            for d in range(n_cells):
                f.write(nc_str_f.format(0))
                f.write('\n')
        f.close()
    with open(path + '/c_n.rom', 'w') as f:
        for t in cn_w:
            for d in t:
                f.write(d)
                f.write('\n')
        if n_threads == 1:
            for d in range(n_cells):
                f.write(cn_str_f.format(0))
                f.write('\n')
        f.close()

    for i in range(n_neighbors):
        with open(path + '/n%d.rom' % i, 'w') as f:
            for c in range(n_cells):
                f.write(n_w[c][i])
                f.write('\n')
            f.close()
