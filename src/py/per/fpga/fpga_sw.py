import random
from src.py.graph.graph_fpga import GraphFGA
from src.py.per.base.per import PeR, EdgesAlgEnum

from src.py.util.util import Util


class FPGAPeR(PeR):
    def __init__(self, graph: GraphFGA):
        super().__init__()
        # random.seed(0)
        self.graph = graph

    def per_sa(self):
        pass

    def per_yoto(self, n_exec: int = 1, edges_alg: EdgesAlgEnum = EdgesAlgEnum.ZIG_ZAG):
        # Final placements
        # placements = []

        # distances histogram
        rel = {}

        # I will initialize the vector with the possible positions for inputs and outputs
        possible_pos_in, possible_pos_out = self.get_in_out_pos()

        # starting executions

        for exe in range(n_exec):
            # First I will start the placement of matrix
            placement = [None for _ in range(self.graph.n_cells)]

            # possible distances to find free cells
            distances_cells = self.graph.get_mesh_distances()

            # Creating the n2c matrix
            n2c = [None for _ in range(self.graph.n_cells)]

            # And then I need to draw the input and output positions
            # They will be randomly placed and the inputs can be on top and left
            # while outputs can be on bottom and right.
            i = 0
            while i < max(len(self.graph.input_nodes), len(self.graph.output_nodes)):
                if i < len(self.graph.input_nodes):
                    n = self.graph.nodes_to_idx[self.graph.input_nodes[i]]
                    ch = self.choose_position(placement, n, possible_pos_in)
                    n2c[n] = ch
                    placement[ch] = n
                if i < len(self.graph.output_nodes):
                    n = self.graph.nodes_to_idx[self.graph.output_nodes[i]]
                    ch = self.choose_position(placement, n, possible_pos_out)
                    n2c[n] = ch
                    placement[ch] = n
                i += 1
            # now, I will start the yoto algorithm.

            # Getting the adges to be placed
            ed_str = []
            if edges_alg == EdgesAlgEnum.ZIG_ZAG:
                ed_str = self.graph.get_edges_zigzag()[0]
            else:
                ed_str = self.graph.get_edges_depth_first()
            ed = self.graph.get_edges_idx(ed_str)

            # if the node that it wants to place is placed, then it will go to next edge

            for e in ed:
                a = e[0]
                b = e[1]
                if n2c[b] is not None:
                    continue
                ai = n2c[a] // self.graph.n_cells_sqrt
                aj = n2c[a] % self.graph.n_cells_sqrt
                # while not find a clear cell, I will try to find one
                distance = 1
                for line in distances_cells:
                    placed = False
                    for ij in line:
                        bi = ai + ij[0]
                        bj = aj + ij[1]
                        if (bi < 0 or bi > self.graph.n_cells_sqrt - 1 or
                                bj < 0 or bj > self.graph.n_cells_sqrt - 1):
                            continue
                        ch = bi * self.graph.n_cells_sqrt + bj
                        if placement[ch] is None:
                            placement[ch] = b
                            n2c[b] = ch
                            placed = True
                            break
                    if placed:
                        break

            h, tc = self.calc_distance(n2c, self.graph.get_edges_idx(self.graph.edges), self.graph.n_cells_sqrt)

            rel[exe] = {
                'exec_id': exe,
                'total_cost': tc,
                'histogram': h,
                'longest_path_cost': self.calc_distance(n2c,
                                                        self.graph.get_edges_idx(self.graph.longest_path),
                                                        self.graph.n_cells_sqrt)[1],
                'longest_path': self.graph.longest_path,
                'longest_path_idx': self.graph.get_nodes_idx(self.graph.longest_path_nodes),
                'nodes_idx': self.graph.nodes_to_idx,
                'placement': placement,
            }
            a = 1
        # TODO Fazer o relatório e os cálculos de distancias, gerar dot.
        for r in rel.keys():
            Util.save_json(Util.get_project_root() + f"/benchmarks/fpga/",
                           f"{self.graph.dot_name}_fpga_yoto_{rel[r]['exec_id']}.txt",
                           rel[r])

    def per_yott(self):
        pass

    def write_dot(self, placement, n2c):
        output_dot_file = self.graph.dot_path + ".placed.dot"
        dot_head = 'digraph layout{\n rankdir=TB;\n splines=ortho;\n node [style=filled shape=square fixedsize=true width=0.6];\n'
        dot_foot = 'edge [constraint=true, style=invis];\n'

        for i in range(self.graph.n_cells_sqrt):
            for j in range(self.graph.n_cells_sqrt):
                dot_foot = dot_foot + '%d' % (j * self.graph.n_cells_sqrt + i)
                if (j + 1) % self.graph.n_cells_sqrt == 0:
                    dot_foot = dot_foot + ';\n'
                else:
                    dot_foot = dot_foot + ' -> '

        for i in range(self.graph.n_cells_sqrt):
            if i % self.graph.n_cells_sqrt == 0:
                dot_foot = dot_foot + 'rank = same {'
            dot_foot = dot_foot + '%d' % i
            if (i + 1) % self.graph.n_cells_sqrt == 0:
                dot_foot = dot_foot + '};\n'
            else:
                dot_foot = dot_foot + ' -> '

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

        for ed in self.graph.edges_idx:
            a = ed[0]
            b = ed[1]
            str_out += f"{n2c[a]} -> {n2c[b]};\n"
        str_out += dot_foot

        with open(output_dot_file, 'w') as f:
            f.write(str_out)
        f.close()

    @staticmethod
    def calc_distance(n2c, edges, cells_sqrt):
        distance = len(edges) * -1
        distances = {}
        for e in edges:
            ia = n2c[e[0]] // cells_sqrt
            ja = n2c[e[0]] % cells_sqrt
            ib = n2c[e[1]] // cells_sqrt
            jb = n2c[e[1]] % cells_sqrt
            dist = FPGAPeR.manhattan_distance(ia, ja, ib, jb)
            if dist not in distances.keys():
                distances[dist] = 0
            distances[dist] += 1
            distance += dist
        return dict(sorted(distances.items())), distance

    @staticmethod
    def manhattan_distance(ia, ja, ib, jb):
        return abs(ia - ib) + abs(ja - jb)

    @staticmethod
    def choose_position(placement, node, choices):
        while True:
            ch = random.choice(choices)
            if placement[ch] is not None:
                continue
            return ch

    def get_in_out_pos(self):
        in_ = []
        out_ = []
        for i in range(self.graph.n_cells_sqrt):
            in_.append(i)
            out_.append(i + self.graph.n_cells - self.graph.n_cells_sqrt)
        for i in range(self.graph.n_cells_sqrt, self.graph.n_cells, self.graph.n_cells_sqrt):
            in_.append(i)
        for i in range(self.graph.n_cells_sqrt - 1, self.graph.n_cells - 1, self.graph.n_cells_sqrt):
            out_.append(i)
        return in_, out_
