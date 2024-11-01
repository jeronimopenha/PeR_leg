//
// Created by jeronimo on 01/11/24.
//

#include "graph.h"

Graph::Graph(const std::string& dot_path, const std::string& dot_name)
    : dot_path_(dot_path), dot_name_(dot_name), n_edges_(0), n_cells_(0), n_cells_sqrt_(0), n_nodes_(0) {
    // Load the graph from .dot file
    Agraph_t* gvc_graph;
    GVC_t* gvc = gvContext();
    gvc_graph = agopen(const_cast<char*>(dot_name.c_str()), Agdirected, nullptr);
    FILE* fp = fopen(dot_path.c_str(), "r");
    agread(fp, gvc_graph);
    fclose(fp);

    // Convert Graphviz graph to Boost graph
    // (Manual edge addition as Boost and Graphviz do not have a direct import link)

    agclose(gvc_graph);
    gvFreeContext(gvc);

    // Initialize graph properties by calling helper methods
    get_nodes_vars();
    get_edges_vars();
    calc_cells_qty();
    n_nodes_ = nodes_str_.size();
}
