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
        # reports
        reports = {}

        t_min = 0.001
        edges = self.graph.get_edges_idx(self.graph.edges_str)
        nodes = self.graph.get_nodes_idx(self.graph.nodes_str)
        for exe in range(n_exec):
            # First I will start the placement of matrix
            placement = [None for _ in range(self.graph.n_cells)]

            possible_cells = [i for i in range(self.graph.n_cells)]

            # Creating the n2c matrix
            n2c = [None for _ in range(self.graph.n_cells)]

            # now I need to place every note in the placement matrix
            self.place_input_output_nodes(n2c, placement)
            for n in self.graph.get_nodes_idx(self.graph.nodes_str):
                if n2c[n] is None:
                    while True:
                        ch = random.choice(possible_cells)
                        if placement[ch] is None:
                            placement[ch] = n
                            n2c[n] = ch
                            break
            t = 100
            h, actual_cost = self.calc_distance(n2c, edges, self.graph.n_cells_sqrt)
            while t >= t_min:
                for cell_a in range(self.graph.n_cells):
                    for cell_b in range(self.graph.n_cells):
                        if (
                                cell_a == cell_b or
                                cell_a in self.possible_pos_in_out and cell_b not in self.possible_pos_in_out or
                                cell_a in self.possible_pos_out and cell_b not in self.possible_pos_out or
                                cell_b in self.possible_pos_in_out and cell_a not in self.possible_pos_in_out or
                                cell_b in self.possible_pos_out and cell_a not in self.possible_pos_out
                        ):
                            continue
                        next_cost = actual_cost
                        a = placement[cell_a]
                        b = placement[cell_b]
                        if a == None and b == None:
                            continue
                        cost_a_b, cost_a_a, cost_b_b, cost_b_a = self.graph.get_cost(n2c, a, b, cell_a, cell_b)

                        next_cost -= cost_a_b
                        next_cost -= cost_b_b
                        next_cost += cost_a_a
                        next_cost += cost_b_a

                        try:
                            valor = exp((-1 * (next_cost - actual_cost) / t))
                        except:
                            valor = -1.0

                        rnd = random.random()

                        if next_cost < actual_cost or rnd <= valor:
                            if a is not None:
                                n2c[a] = cell_b

                            if b is not None:
                                n2c[b] = cell_a
                            placement[cell_a], placement[cell_b] = placement[cell_b], placement[cell_a]

                            # = sa_graph.get_total_cost(c_n[thread], n_c[thread])
                            actual_cost = next_cost
                            # print(actual_cost)
                        a = 1
                    t *= 0.999
            reports[exe] = {
                'exec_id': exe,
                'total_cost': actual_cost,
                'histogram': h,
                'longest_path_cost': self.calc_distance(n2c,
                                                        self.graph.get_edges_idx(self.graph.longest_path),
                                                        self.graph.n_cells_sqrt, len(self.graph.nodes_str))[1],
                'longest_path': self.graph.longest_path,
                'longest_path_idx': self.graph.get_nodes_idx(self.graph.longest_path_nodes),
                'nodes_idx': self.graph.nodes_to_idx,
                'placement': placement,
            }
            a = 1
        # TODO Melhorar isso
        for r in reports.keys():
            Util.write_json(Util.get_project_root() + f"/benchmarks/fpga/",
                            f"{self.graph.dot_name}_fpga_sa_{reports[r]['exec_id']}.txt",
                            reports[r])

    def per_yoto(self, n_exec: int = 1, edges_alg: EdgesAlgEnum = EdgesAlgEnum.ZIG_ZAG_NO_PRIORITY,
                 pre_placed_in: bool = False):
        # Final placements
        # placements = []

        # reports
        reports = {}

        input_nodes_idx = self.graph.get_nodes_idx(self.graph.input_nodes)
        output_nodes_idx = self.graph.get_nodes_idx(self.graph.output_nodes)

        # starting executions
        for exec_id in range(n_exec):
            # First I will start the placement of matrix
            placement = [None for _ in range(self.graph.n_cells)]

            # possible distances to find free cells
            distances_cells = self.graph.get_mesh_distances()

            # Creating the n2c matrix
            n2c = [None for _ in range(self.graph.n_cells)]

            # Getting the edges to be placed
            ed_str = []
            if edges_alg == EdgesAlgEnum.ZIG_ZAG_NO_PRIORITY:
                ed_str = self.graph.get_edges_zigzag_no_priority()[0]
            else:
                ed_str = self.graph.get_edges_depth_first_no_priority()
            ed = self.graph.get_edges_idx(ed_str)

            # And then I need to draw the input and output positions
            # They will be randomly placed and the inputs can be on top and left
            # while outputs can be on bottom and right.
            self.place_input_output_nodes(n2c, placement, pre_placed_in)

            # now, I will start the yoto algorithm.

            # if the node that it wants to place is placed, then it will go to next edge

            for e in ed:
                a = e[0]
                b = e[1]
                if n2c[b] is not None:
                    continue
                ai = n2c[a] // self.graph.n_cells_sqrt
                aj = n2c[a] % self.graph.n_cells_sqrt
                # while not find a clear cell, I will try to find one

                flag = False
                for l_n,line in enumerate(distances_cells):
                    placed = False
                    for ij in line:
                        bi = ai + ij[0]
                        bj = aj + ij[1]
                        if (bi < 0 or bi > self.graph.n_cells_sqrt - 1 or
                                bj < 0 or bj > self.graph.n_cells_sqrt - 1):
                            continue
                        ch = bi * self.graph.n_cells_sqrt + bj
                        if ch in self.possible_pos_in_out:
                            if b not in input_nodes_idx and b not in output_nodes_idx:
                                continue
                        if placement[ch] is None:
                            placement[ch] = b
                            n2c[b] = ch
                            placed = True
                            break
                    if placed:
                        flag = True
                        break
            h, tc = self.calc_distance(n2c, ed, self.graph.n_cells_sqrt, len(self.graph.nodes_str))

            reports[exec_id] = {
                'exec_id': exec_id,
                'dot_name': self.graph.dot_name,
                'dot_path': self.graph.dot_path,
                'placer': 'yoto',
                'edges_algorithm': edges_alg.name,
                'pre_placed_in_out': pre_placed_in,
                'total_cost': tc,
                'histogram': h,
                'longest_path_cost': self.calc_distance(n2c,
                                                        self.graph.get_edges_idx(self.graph.longest_path),
                                                        self.graph.n_cells_sqrt, len(self.graph.nodes_str))[1],
                'longest_path': self.graph.longest_path,
                'longest_path_idx': self.graph.get_nodes_idx(self.graph.longest_path_nodes),
                'nodes_idx': self.graph.nodes_to_idx,
                'placement': placement,
                'n2c': n2c,
            }
        return reports

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

        input_nodes = [self.graph.nodes_to_idx[node] for node in self.graph.input_nodes]
        output_nodes = [self.graph.nodes_to_idx[node] for node in self.graph.output_nodes]

        for i in range(self.graph.n_cells):
            if placement[i] in input_nodes:
                str_out += '%d[label="%d", fontsize=8, fillcolor="%s"];\n' % (
                    i, placement[i], '#d9d9d9')  ##ffffff')  # if int(c_content, 16) == 0 else '#d9d9d9')
            elif placement[i] in output_nodes:
                str_out += '%d[label="%d", fontsize=8, fillcolor="%s"];\n' % (
                    i, placement[i], '#d9d9ff')  ##ffffff')  # if int(c_content, 16) == 0 else '#d9d9d9')
            else:
                str_out += '%d[label="%d", fontsize=8, fillcolor="%s"];\n' % (
                    i, placement[i], '#ffffff')
        str_out += 'edge [constraint=false, style=vis];'
        for ed in self.graph.get_edges_idx(self.graph.edges_str):
            a = ed[0]
            b = ed[1]
            str_out += f"{n2c[a]} -> {n2c[b]};\n"
        str_out += dot_foot

        with open(output_dot_file, 'w') as f:
            f.write(str_out)
        f.close()

    def place_input_output_nodes(self, n2c, placement, pre_placed_in):
        output_nodes = self.graph.get_nodes_idx(self.graph.output_nodes)
        i = 0
        while i < len(output_nodes):
            if i < len(output_nodes):
                n = output_nodes[i]
                while True:
                    ch = self.choose_position(placement,  self.possible_pos_in_out)
                    if placement[ch] is None:
                        placement[ch] = n
                        n2c[n] = ch
                        break
            i += 1
        if pre_placed_in:
            input_nodes = self.graph.get_nodes_idx(self.graph.input_nodes)
            i = 0
            while i < len(input_nodes):
                if i < len(input_nodes):
                    n = input_nodes[i]
                    while True:
                        ch = self.choose_position(placement,  self.possible_pos_in_out)
                        if placement[ch] is None:
                            placement[ch] = n
                            n2c[n] = ch
                            break
                    i += 1

    @staticmethod
    def calc_distance(n2c, edges, cells_sqrt, n_nodes):
        distance = len(edges) * -1
        distances = {}
        counter = 0
        for e in edges:
            if counter >= n_nodes-1:
                break
            ia = n2c[e[0]] // cells_sqrt
            ja = n2c[e[0]] % cells_sqrt
            ib = n2c[e[1]] // cells_sqrt
            jb = n2c[e[1]] % cells_sqrt
            dist = FPGAPeR.manhattan_distance(ia, ja, ib, jb)
            if dist not in distances.keys():
                distances[dist] = 0
            distances[dist] += 1
            distance += dist
            counter +=1
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
