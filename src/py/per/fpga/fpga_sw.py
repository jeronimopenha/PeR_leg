import multiprocessing
import os
import random

from math import exp

from src.py.graph.graph_fpga import GraphFGA
from src.py.per.base.per import PeR, EdgesAlgEnum

from src.py.util.util import Util


class FPGAPeR(PeR):
    def __init__(self, graph: GraphFGA):
        super().__init__()
        # random.seed(0)
        self.graph = graph
        # I will initialize the vector with the possible positions for inputs and outputs
        self.possible_pos_in_out = []
        self.get_in_out_pos()

    def per_sa(self, n_exec: int = 1):
        # Initialize multiprocessing
        manager = multiprocessing.Manager()
        report = manager.dict()  # Shared report dictionary
        lock = multiprocessing.Lock()  # Lock for synchronized access
        num_workers = multiprocessing.cpu_count()

        # List to hold process references
        processes = []

        # Spawn processes for each exec_id
        for exec_id in range(n_exec):
            p = multiprocessing.Process(target=FPGAPeR.per_sa_worker, args=(self, exec_id, report, lock))
            processes.append(p)
            p.start()

            # Limit the number of concurrent workers
            if len(processes) >= num_workers:
                for proc in processes:
                    proc.join()  # Wait for all workers to finish
                processes = []  # Reset the list for the next batch

        # Wait for the remaining processes to finish
        for proc in processes:
            proc.join()
        rep = dict(report)
        return rep

    def per_sa_worker(cls, exec_id, report, lock):
        # report
        t_min = 0.001
        t = 100

        # First I will start the placement of matrix
        placement = [None for _ in range(cls.graph.n_cells)]

        possible_base_cells = [i for i in range(cls.graph.n_cells)]
        possible_base_cells = [cell for cell in possible_base_cells if cell not in cls.possible_pos_in_out]
        # Creating the n2c matrix
        n2c = [None for _ in range(cls.graph.n_nodes)]

        # now I need to place every note in the placement matrix
        # self.place_input_output_nodes(n2c, placement)
        for n in cls.graph.get_nodes_idx(cls.graph.nodes_str):
            if n2c[n] is None:
                while True:
                    if n in cls.graph.input_nodes_idx or n in cls.graph.output_nodes_idx:
                        ch = random.choice(cls.possible_pos_in_out)
                    else:
                        ch = random.choice(possible_base_cells)
                    if placement[ch] is None:
                        placement[ch] = n
                        n2c[n] = ch
                        break

        while t >= t_min:
            for cell_a in range(cls.graph.n_cells):
                for cell_b in range(cls.graph.n_cells):
                    if (
                            cell_a == cell_b or
                            (cell_a in cls.possible_pos_in_out and cell_b not in cls.possible_pos_in_out) or
                            (cell_b in cls.possible_pos_in_out and cell_a not in cls.possible_pos_in_out)
                    ):
                        continue
                    a = placement[cell_a]
                    b = placement[cell_b]
                    if a == None and b == None:
                        continue
                    cost_a_b, cost_a_a, cost_b_b, cost_b_a = cls.graph.get_cost(n2c, a, b, cell_a, cell_b)

                    cost_a = cost_a_a + cost_b_a
                    cost_b = cost_a_b + cost_b_b

                    try:
                        valor = exp((-1 * (cost_a - cost_b) / t))
                    except:
                        valor = -1.0

                    rnd = random.random()

                    if cost_a < cost_b or rnd <= valor:
                        if a is not None:
                            n2c[a] = cell_b

                        if b is not None:
                            n2c[b] = cell_a
                        placement[cell_a], placement[cell_b] = placement[cell_b], placement[cell_a]
                        # print(t, actual_cost)
                        # self.write_dot('/home/jeronimo/GIT/PeR/reports/fpga/', f"_placed.dot",
                        #               placement, n2c)
                t *= 0.999
        h, tc = cls.calc_distance(n2c, cls.graph.edges_idx, cls.graph.n_cells_sqrt, cls.graph.n_nodes)

        # Write to the shared report with a lock
        with lock:
            report[exec_id] = {
                'exec_id': exec_id,
                'dot_name': cls.graph.dot_name,
                'dot_path': cls.graph.dot_path,
                'placer': 'sa',
                'edges_algorithm': "direct",
                'total_cost': tc,
                'histogram': h,
                'longest_path_cost': cls.calc_distance(n2c,
                                                       cls.graph.get_edges_idx(cls.graph.longest_path),
                                                       cls.graph.n_cells_sqrt, cls.graph.n_nodes)[1],
                'longest_path': cls.graph.longest_path,
                'longest_path_idx': cls.graph.get_nodes_idx(cls.graph.longest_path_nodes),
                'nodes_idx': cls.graph.nodes_to_idx,
                'placement': placement,
                'n2c': n2c,
                'edges': cls.graph.edges_idx,
                #'neigh': cls.graph.neighbors_idx
            }

    def per_yoto(self, n_exec: int = 1, edges_alg: EdgesAlgEnum = EdgesAlgEnum.ZIG_ZAG_NO_PRIORITY):
        # Initialize multiprocessing
        manager = multiprocessing.Manager()
        report = manager.dict()  # Shared report dictionary
        lock = multiprocessing.Lock()  # Lock for synchronized access
        num_workers = multiprocessing.cpu_count()

        # List to hold process references
        processes = []

        # Spawn processes for each exec_id
        for exec_id in range(n_exec):
            p = multiprocessing.Process(target=FPGAPeR.per_yoto_worker, args=(self, exec_id, edges_alg, report, lock))
            processes.append(p)
            p.start()

            # Limit the number of concurrent workers
            if len(processes) >= num_workers:
                for proc in processes:
                    proc.join()  # Wait for all workers to finish
                processes = []  # Reset the list for the next batch

        # Wait for the remaining processes to finish
        for proc in processes:
            proc.join()

        return dict(report)

    def per_yoto_worker(cls, exec_id, edges_alg, report, lock):
        # Prepare the report
        placement = [None for _ in range(cls.graph.n_cells)]
        distances_cells = cls.graph.get_mesh_distances()
        n2c = [None for _ in range(cls.graph.n_nodes)]

        # Getting the edges to be placed
        ed_str = []
        if edges_alg == EdgesAlgEnum.DEPTH_FIRST_NO_PRIORITY:
            ed_str = cls.graph.get_edges_depth_first()
        elif edges_alg == EdgesAlgEnum.DEPTH_FIRST_WITH_PRIORITY:
            ed_str = cls.graph.get_edges_depth_first(with_priority=True)
        elif edges_alg == EdgesAlgEnum.ZIG_ZAG_NO_PRIORITY:
            ed_str = cls.graph.get_edges_zigzag()[0]
        elif edges_alg == EdgesAlgEnum.ZIG_ZAG_WITH_PRIORITY:
            ed_str = cls.graph.get_edges_zigzag(with_priority=True)[0]
        ed = cls.graph.get_edges_idx(ed_str)

        # Input and output position placement
        if edges_alg == EdgesAlgEnum.DEPTH_FIRST_NO_PRIORITY or edges_alg == EdgesAlgEnum.DEPTH_FIRST_WITH_PRIORITY:
            cls.place_input_output_nodes(n2c, placement)
        elif edges_alg == EdgesAlgEnum.ZIG_ZAG_NO_PRIORITY or edges_alg == EdgesAlgEnum.ZIG_ZAG_WITH_PRIORITY:
            ch = cls.choose_position(placement, cls.possible_pos_in_out)
            placement[ch] = ed[0][0]
            n2c[ed[0][0]] = ch

        # Yoto algorithm logic
        for e in ed:
            a = e[0]
            b = e[1]
            if n2c[b] is not None:
                continue
            if n2c[a] is None:
                a = 1
            ai = n2c[a] // cls.graph.n_cells_sqrt
            aj = n2c[a] % cls.graph.n_cells_sqrt

            flag = False
            for l_n, line in enumerate(distances_cells):
                placed = False
                for ij in line:
                    bi = ai + ij[0]
                    bj = aj + ij[1]
                    if (bi < 0 or bi >= cls.graph.n_cells_sqrt or
                            bj < 0 or bj >= cls.graph.n_cells_sqrt or
                            (bi == 0 and (bj == 0 or bj == cls.graph.n_cells_sqrt)) or
                            (bj == 0 and (bi == 0 or bi == cls.graph.n_cells_sqrt))):
                        continue
                    ch = bi * cls.graph.n_cells_sqrt + bj
                    if ch in cls.possible_pos_in_out:
                        if b not in cls.graph.input_nodes_idx and b not in cls.graph.output_nodes_idx:
                            continue
                    else:
                        if b in cls.graph.input_nodes_idx or b in cls.graph.output_nodes_idx:
                            continue
                    if placement[ch] is None:
                        placement[ch] = b
                        n2c[b] = ch
                        placed = True
                        break
                if placed:
                    flag = True
                    break

        h, tc = cls.calc_distance(n2c, cls.graph.edges_idx, cls.graph.n_cells_sqrt, cls.graph.n_nodes)

        # Write to the shared report with a lock
        with lock:
            report[exec_id] = {
                'exec_id': exec_id,
                'dot_name': cls.graph.dot_name,
                'dot_path': cls.graph.dot_path,
                'placer': 'yoto',
                'edges_algorithm': edges_alg.name,
                'total_cost': tc,
                'histogram': h,
                'longest_path_cost': cls.calc_distance(n2c,
                                                       cls.graph.get_edges_idx(cls.graph.longest_path),
                                                       cls.graph.n_cells_sqrt, cls.graph.n_nodes)[1],
                'longest_path': cls.graph.longest_path,
                'longest_path_idx': cls.graph.get_nodes_idx(cls.graph.longest_path_nodes),
                'nodes_idx': cls.graph.nodes_to_idx,
                'input_nodes': cls.graph.input_nodes_idx,
                'output_nodes': cls.graph.output_nodes_idx,
                'placement': placement,
                'n2c': n2c,
                'edges': cls.graph.edges_idx,
                #'neigh': cls.graph.neighbors_idx
            }

    def per_yott(self):
        pass

    def write_dot(self, path, file_name, placement, n2c):
        path = Util.verify_path(path)
        output_dot_file = path + file_name
        dot_head = 'digraph layout{\n rankdir=TB;\n splines=ortho;\n node [style=filled shape=square fixedsize=true width=0.6];\n'
        dot_foot = 'edge [constraint=true, style=invis];\n'

        for i in range(self.graph.n_cells_sqrt):
            for j in range(self.graph.n_cells_sqrt):
                dot_foot = dot_foot + '%d' % (j * self.graph.n_cells_sqrt + i)
                if (j + 1) % self.graph.n_cells_sqrt == 0:
                    dot_foot = dot_foot + ';\n'
                else:
                    dot_foot = dot_foot + ' -> '

        for i in range(self.graph.n_cells):
            if i % self.graph.n_cells_sqrt == 0:
                dot_foot += 'rank = same {'
            dot_foot = dot_foot + '%d' % i
            if (i + 1) % self.graph.n_cells_sqrt == 0:
                dot_foot += '};\n'
            else:
                dot_foot += ' -> '

        dot_foot = dot_foot + '}'

        str_out = dot_head

        input_nodes = [self.graph.nodes_to_idx[node] for node in self.graph.input_nodes_str]
        output_nodes = [self.graph.nodes_to_idx[node] for node in self.graph.output_nodes]

        for i in range(self.graph.n_cells):
            if placement[i] is None:
                str_out += '%d[label="%d", fontsize=8, fillcolor="%s"];\n' % (
                    i, i, '#ffffff')
            elif placement[i] in input_nodes:
                str_out += '%d[label="%d", fontsize=8, fillcolor="%s"];\n' % (
                    i, placement[i],
                    '#e3c9af')  ##ffffff')  # if int(c_content, 16) == 0 else '#d9d9d9')
            elif placement[i] in output_nodes:
                str_out += '%d[label="%d", fontsize=8, fillcolor="%s"];\n' % (
                    i, placement[i],
                    '#a9ccde')  ##ffffff')  # if int(c_content, 16) == 0 else '#d9d9d9')
            else:
                str_out += '%d[label="%d", fontsize=8, fillcolor="%s"];\n' % (
                    i, placement[i], '#91e3bb')
        str_out += 'edge [constraint=false, style=vis];'
        for ed in self.graph.get_edges_idx(self.graph.edges_str):
            a = ed[0]
            b = ed[1]
            str_out += f"{n2c[a]} -> {n2c[b]};\n"
        str_out += dot_foot

        with open(output_dot_file, 'w') as f:
            f.write(str_out)
        f.close()

    def place_input_output_nodes(self, n2c, placement):
        output_nodes = self.graph.get_nodes_idx(self.graph.output_nodes)
        i = 0
        while i < len(output_nodes):
            if i < len(output_nodes):
                n = output_nodes[i]
                while True:
                    ch = self.choose_position(placement, self.possible_pos_in_out)
                    if placement[ch] is None:
                        placement[ch] = n
                        n2c[n] = ch
                        break
            i += 1

    @staticmethod
    def calc_distance(n2c, edges, cells_sqrt, n_nodes):
        distance = 0
        distances = {}
        counter = 0
        for e in edges:
            if counter >= n_nodes - 1:
                break
            dist = GraphFGA.get_manhattan_distance(n2c[e[0]], n2c[e[1]], cells_sqrt)
            if dist not in distances.keys():
                distances[dist] = 0
            distances[dist] += 1
            distance += dist
            counter += 1
        return dict(sorted(distances.items())), distance

    @staticmethod
    def manhattan_distance(ia, ja, ib, jb):
        return abs(ia - ib) + abs(ja - jb)

    @staticmethod
    def choose_position(placement, choices):
        while True:
            ch = random.choice(choices)
            if placement[ch] is not None:
                continue
            return ch

    def get_in_out_pos(self):
        in_out = []
        for i in range(self.graph.n_cells_sqrt):
            in_out.append(i)
        for i in range(self.graph.n_cells_sqrt):
            in_out.append(i + self.graph.n_cells - self.graph.n_cells_sqrt)
        for i in range(self.graph.n_cells_sqrt, self.graph.n_cells - self.graph.n_cells_sqrt, self.graph.n_cells_sqrt):
            in_out.append(i)
        for i in range(self.graph.n_cells_sqrt * 2 - 1, self.graph.n_cells - 1, self.graph.n_cells_sqrt):
            in_out.append(i)
        self.possible_pos_in_out = in_out
