#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <unordered_map>
#include <random>

#include "src/util/per_enum.hpp"
#include "src/python/util/per_graph.hpp"
#include "src/util/util.hpp"

class PiplineBase {
private:
    int len_pipeline;
    PeRGraph per_graph;
    ArchType arch_type;
    int distance_table_bits;
    bool make_shuffle;
    int n_threads;
public:
    PiplineBase(PeRGraph per_graph, ArchType arch_type, int distance_table_bits, bool make_shuffle, int len_pipeline, int n_threads)
        : len_pipeline(len_pipeline), per_graph(per_graph), arch_type(arch_type), distance_table_bits(distance_table_bits), make_shuffle(make_shuffle), n_threads(n_threads) {
        edges_raw.resize(len_pipeline);
        edges_str.resize(len_pipeline);
        edges_int.resize(len_pipeline);
        annotations.resize(len_pipeline);

        for (int i = 0; i < len_pipeline; ++i) {
            auto [edges_str_i, edges_raw_i, rec_i] = per_graph.get_edges_zigzag(make_shuffle);
            edges_str[i] = edges_str_i;
            edges_raw[i] = edges_raw_i;
            edges_int[i] = get_edges_int(edges_str_i);
            annotations[i] = Util::get_graph_annotations(edges_raw_i, rec_i);
        }

        visited_edges = edges_int[0].size();
        total_edges = edges_raw[0].size();

        n_lines = std::sqrt(per_graph.n_cells);
        n_columns = n_lines;
        line_bits = std::sqrt(per_graph.n_cells);
        column_bits = line_bits;
    }

    std::vector<std::vector<int>> get_edges_int(std::vector<std::vector<int>> edges_str) {
        std::vector<std::vector<int>> edges_int;
        for (auto &edge : edges_str) {
            edges_int.push_back({per_graph.nodes_to_idx[edge[0]], per_graph.nodes_to_idx[edge[1]]});
        }
        return edges_int;
    }

    std::tuple<std::vector<std::vector<int>>, std::vector<std::vector<int>>> init_sa_placement_tables() {
        std::vector<std::vector<int>> n2c, c2n;
        for (int i = 0; i < n_threads; ++i) {
            std::vector<int> n2c_tmp(n_lines * n_columns, -1);
            std::vector<int> c2n_tmp(n_lines * n_columns, -1);

            std::vector<int> cells(per_graph.n_cells);
            std::iota(cells.begin(), cells.end(), 0);
            std::shuffle(cells.begin(), cells.end(), std::mt19937(std::random_device()()));

            for (auto &node : per_graph.nodes) {
                int random_cell = cells.back();
                cells.pop_back();
                c2n_tmp[random_cell] = per_graph.nodes_to_idx[node];
                n2c_tmp[c2n_tmp[random_cell]] = random_cell;
            }

            n2c.push_back(n2c_tmp);
            c2n.push_back(c2n_tmp);
        }
        return {n2c, c2n};
    }

    std::tuple<std::vector<std::vector<std::vector<int>>>, std::vector<std::vector<int>>> init_traversal_placement_tables(std::vector<int> first_node) {
        std::vector<std::vector<std::vector<int>>> n2c;
        std::vector<std::vector<int>> c2n;
        for (int i = 0; i < len_pipeline; ++i) {
            std::vector<std::vector<int>> n2c_tmp(per_graph.n_cells, std::vector<int>(2, -1));
            std::vector<std::vector<int>> c2n_tmp(n_lines, std::vector<int>(n_lines, -1));

            int idx_i, idx_j;
            Util::get_line_column_cell_sqrt(std::rand() % per_graph.n_cells, n_lines, idx_i, idx_j);
            n2c_tmp[first_node[i]][0] = idx_i;
            n2c_tmp[first_node[i]][1] = idx_j;
            c2n_tmp[idx_i][idx_j] = first_node[i];

            n2c.push_back(n2c_tmp);
            c2n.push_back(c2n_tmp);
        }
        return {n2c, c2n};
    }

    std::tuple<bool, std::vector<std::vector<std::vector<int>>>, std::unordered_map<std::string, std::vector<int>>> routing_mesh(std::vector<std::vector<int>> edges, std::vector<std::vector<int>> positions) {
        int n_cells = per_graph.n_cells;
        int n_cells_sqrt = std::sqrt(n_cells);
        std::vector<std::vector<std::vector<int>>> grid(n_cells, std::vector<std::vector<int>>(4, std::vector<int>(1, -1)));
        std::unordered_map<std::string, std::vector<int>> dic_path;

        for (int j = 0; j < edges.size(); ++j) {
            int a = edges[j][0];
            int b = edges[j][1];
            std::string key = std::to_string(edges[j][0]) + "_" + std::to_string(edges[j][1]);
            int pos_a_i = positions[a][0];
            int pos_a_j = positions[a][1];
            int pos_b_i = positions[b][0];
            int pos_b_j = positions[b][1];

            dic_path[key] = {};
            int dist_walk = -1;

            int dist_i = std::abs(pos_b_i - pos_a_i);
            int dist_j = std::abs(pos_b_j - pos_a_j);

            int pos_node_i = pos_a_i;
            int pos_node_j = pos_a_j;
            bool change = false;

            std::vector<int> count_per_curr;
            while (dist_i != 0 || dist_j != 0) {
                int diff_i = pos_b_i - pos_node_i;
                int diff_j = pos_b_j - pos_node_j;
                int pe_curr = pos_node_i * n_cells_sqrt + pos_node_j;
                dic_path[key].push_back(pe_curr);
                count_per_curr.push_back(pe_curr);

                if (diff_j > 0 && pe_curr + 1 < (pos_node_i + 1) * n_cells_sqrt && (grid[pe_curr][1][0] == -1 || grid[pe_curr][1][0] == a) && grid[pe_curr + 1][3][0] != a && std::find(count_per_curr.begin(), count_per_curr.end(), pe_curr + 1) == count_per_curr.end()) {
                    grid[pe_curr][1][0] = a;
                    pos_node_j += 1;
                    change = true;
                } else if (diff_j < 0 && pe_curr - 1 >= pos_node_i * n_cells_sqrt && (grid[pe_curr][3][0] == -1 || grid[pe_curr][3][0] == a) && grid[pe_curr - 1][1][0] != a && std::find(count_per_curr.begin(), count_per_curr.end(), pe_curr - 1) == count_per_curr.end()) {
                    grid[pe_curr][3][0] = a;
                    pos_node_j -= 1;
                    change = true;
                } else if (diff_i > 0 && pe_curr + n_cells_sqrt < n_cells && (grid[pe_curr][2][0] == -1 || grid[pe_curr][2][0] == a) && grid[pe_curr + n_cells_sqrt][0][0] != a && std::find(count_per_curr.begin(), count_per_curr.end(), pe_curr + n_cells_sqrt) == count_per_curr.end()) {
                    grid[pe_curr][2][0] = a;
                    pos_node_i += 1;
                    change = true;
                } else if (diff_i < 0 && pe_curr - n_cells_sqrt >= 0 && (grid[pe_curr][0][0] == -1 || grid[pe_curr][0][0] == a) && grid[pe_curr - n_cells_sqrt][2][0] != a && std::find(count_per_curr.begin(), count_per_curr.end(), pe_curr - n_cells_sqrt) == count_per_curr.end()) {
                    grid[pe_curr][0][0] = a;
                    pos_node_i -= 1;
                    change = true;
                }

                if (!change) {
                    if (pe_curr + 1 < (pos_node_i + 1) * n_cells_sqrt && (grid[pe_curr][1][0] == -1 || grid[pe_curr][1][0] == a) && grid[pe_curr + 1][3][0] != a && std::find(count_per_curr.begin(), count_per_curr.end(), pe_curr + 1) == count_per_curr.end()) {
                        grid[pe_curr][1][0] = a;
                        pos_node_j += 1;
                        change = true;
                    } else if (pe_curr - 1 >= pos_node_i * n_cells_sqrt && (grid[pe_curr][3][0] == -1 || grid[pe_curr][3][0] == a) && grid[pe_curr - 1][1][0] != a && std::find(count_per_curr.begin(), count_per_curr.end(), pe_curr - 1) == count_per_curr.end()) {
                        grid[pe_curr][3][0] = a;
                        pos_node_j -= 1;
                        change = true;
                    } else if (pe_curr + n_cells_sqrt < n_cells && (grid[pe_curr][2][0] == -1 || grid[pe_curr][2][0] == a) && grid[pe_curr + n_cells_sqrt][0][0] != a && std::find(count_per_curr.begin(), count_per_curr.end(), pe_curr + n_cells_sqrt) == count_per_curr.end()) {
                        grid[pe_curr][2][0] = a;
                        pos_node_i += 1;
                        change = true;
                    } else if (pe_curr - n_cells_sqrt >= 0 && (grid[pe_curr][0][0] == -1 || grid[pe_curr][0][0] == a) && grid[pe_curr - n_cells_sqrt][2][0] != a && std::find(count_per_curr.begin(), count_per_curr.end(), pe_curr - n_cells_sqrt) == count_per_curr.end()) {
                        grid[pe_curr][0][0] = a;
                        pos_node_i -= 1;
                        change = true;
                    }
                }

                if (!change) {
                    return {false, grid, dic_path};
                }

                dist_i = std::abs(pos_b_i - pos_node_i);
                dist_j = std::abs(pos_b_j - pos_node_j);
                dist_walk++;
                change = false;
            }

            if (change) {
                return {false, grid, dic_path};
            }
        }

        return {true, grid, dic_path};
    }

private:
    std::vector<std::vector<std::vector<int>>> edges_raw;
    std::vector<std::vector<std::vector<int>>> edges_str;
    std::vector<std::vector<std::vector<int>>> edges_int;
    std::vector<std::unordered_map<std::string, std::vector<int>>> annotations;
    int visited_edges;
    int total_edges;
    int n_lines;
    int n_columns;
    int line_bits;
    int column_bits;
};