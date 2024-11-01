//
// Created by jeronimo on 01/11/24.
//

#ifndef GRAPH_H
#define GRAPH_H

#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/directed_graph.hpp>
#include <graphviz/gvc.h>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>
#include <cmath>
#include <random>
#include <iostream>
#include <fstream>

class Graph {
public:
    Graph(const std::string& dot_path, const std::string& dot_name);

    // Public methods (equivalent to the Python methods)
    void clear_graph();
    void get_nodes_vars();
    void get_edges_vars();
    void calc_cells_qty();
    std::vector<std::pair<int, int>> get_edges_idx(const std::vector<std::pair<std::string, std::string>>& edges);
    std::vector<int> get_nodes_idx(const std::vector<std::string>& nodes);
    std::vector<std::vector<int>> get_mesh_distances(bool make_shuffle = true);
    static std::vector<std::vector<int>> format_distance_table(const std::vector<std::vector<int>>& distance_table_raw, bool make_shuffle);
    std::vector<std::pair<int, int>> get_edges_depth_first(bool make_shuffle = true, bool with_priority = false);
    std::pair<std::vector<std::pair<int, int>>, std::vector<std::pair<int, int>>> get_edges_zigzag(bool make_shuffle = true);
    static std::vector<std::vector<int>> clear_edges(const std::vector<std::vector<int>>& edges, bool remove_placed_edges = true);
    int get_cost(int n_c, int node1, int node2, int cell1, int cell2);
    static int get_manhattan_distance(int cell1, int cell2, int n_cells_sqrt);
    void longest_path_and_length();
    std::unordered_map<int, std::vector<std::vector<int>>> get_graph_annotations(const std::vector<std::vector<int>>& edges, const std::vector<std::vector<int>>& convergences);

private:
    // Data members
    std::string dot_path_;
    std::string dot_name_;
    boost::adjacency_list<boost::vecS, boost::vecS, boost::directedS> g_; // Boost directed graph
    std::vector<std::string> nodes_str_;
    std::vector<std::pair<std::string, std::string>> edges_str_;
    int n_edges_;
    std::unordered_map<std::string, int> nodes_to_idx_;
    std::unordered_map<int, std::string> idx_to_nodes_;
    std::unordered_map<int, std::vector<std::string>> neighbors_str_;
    std::unordered_map<int, std::vector<int>> neighbors_idx_;
    std::unordered_map<int, std::vector<int>> dir_neighbors_str_;
    std::unordered_map<int, std::vector<int>> dir_neighbors_idx_;
    std::vector<std::string> input_nodes_str_;
    std::vector<std::string> output_nodes_str_;
    int n_cells_;
    int n_cells_sqrt_;
    int n_nodes_;
    std::vector<int> input_nodes_idx_;
    std::vector<int> output_nodes_idx_;
    std::vector<std::pair<int, int>> edges_idx_;
    std::vector<int> longest_path_;
    std::vector<std::pair<int, int>> longest_path_nodes_;

    // Helper functions
    static std::string func_key(const std::string& val1, const std::string& val2);
    static std::vector<std::string> func_unkey(const std::string& text);
};


#endif //GRAPH_H
