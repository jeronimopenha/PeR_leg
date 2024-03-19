#include "util_sa_hls.hpp"

void get_line_column_from_cell(ap_int<8> cell, ap_int<8> n_lines, ap_int<8> n_columns, ap_int<8> &line, ap_int<8> &column)
{
#pragma HLS INLINE
    line = cell / n_lines;
    column = cell % n_columns;
}

ap_int<8> dist_manhattan(ap_int<8> ia, ap_int<8> ja, ap_int<8> ib, ap_int<8> jb)
{
#pragma HLS INLINE
    return abs(ia - ib) + abs(ja - jb);
}

ap_int<8> dist_one_hop(ap_int<8> ia, ap_int<8> ja, ap_int<8> ib, ap_int<8> jb)
{
#pragma HLS INLINE
    ap_int<8> i = abs(ia - ib);
    ap_int<8> j = abs(ja - jb);
    return (ap_int<8>)ceil(i / 2.0) + (ap_int<8>)ceil(j / 2.0);
}