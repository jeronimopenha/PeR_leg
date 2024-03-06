//
// Created by jeronimo on 04/03/24.
//

#ifndef CPP_SA_PIPELINE_SW_H
#define CPP_SA_PIPELINE_SW_H

#include <cmath>
#include <cstring>
#include "util.h"

#define TH_BITS (int)ceil(log2(N_THREADS))
#define CELL_BITS (int)ceil(log2(N_CELLS))
#define MASK (N_CELLS_POW-1)

#define N_NEIGH 4
#define N_THREADS 6
#define N_CELLS  100
#define N_CELLS_SQRT 10
#define N_CELLS_POW 10000
#define N_LINES N_CELLS_SQRT
#define N_COLUMNS N_CELLS_SQRT
#define N_COPIES 1
#define MESH 0
#define ONE_HOP 1
#define ARCH_TYPE MESH

struct W {
    int th_idx;
    int cell;
    int node;
};

struct ST0_OUT {
    int th_idx;
    bool th_valid;
    int cell_a;
    int cell_b;
};

struct ST9_OUT {
    int th_idx;
    bool th_valid;
    bool sw;
};

struct ST1_OUT {
    int th_idx;
    bool th_valid;
    int cell_a;
    int cell_b;
    int node_a;
    int node_b;
    ST9_OUT sw;
    W wa;
    W wb;
};

struct ST2_OUT {
    int th_idx;
    bool th_valid;
    int cell_a;
    int cell_b;
    int node_a;
    int node_b;
    int va[N_NEIGH];
    int vb[N_NEIGH];
    ST9_OUT sw;
    W wa;
    W wb;
};

struct ST3_OUT {
    int th_idx;
    bool th_valid;
    int cell_a;
    int cell_b;
    int cva[N_NEIGH];
    int cvb[N_NEIGH];
    ST9_OUT sw;
    W wa;
    W wb;
};

struct ST4_OUT {
    int th_idx;
    bool th_valid;
    int cell_a;
    int cell_b;
    int cva[N_NEIGH];
    int cvb[N_NEIGH];
    int dvac[N_NEIGH];
    int dvbc[N_NEIGH];
};

struct ST5_OUT {
    int th_idx;
    bool th_valid;
    int dvac[N_NEIGH / 2];
    int dvbc[N_NEIGH / 2];
    int dvas[N_NEIGH];
    int dvbs[N_NEIGH];
};

struct ST6_OUT {
    int th_idx;
    bool th_valid;
    int dvac;
    int dvbc;
    int dvas[N_NEIGH / 2];
    int dvbs[N_NEIGH / 2];
};

struct ST7_OUT {
    int th_idx;
    bool th_valid;
    int dc;
    int dvas;
    int dvbs;
};

struct ST8_OUT {
    int th_idx;
    bool th_valid;
    int dc;
    int ds;
};
#endif //CPP_SA_PIPELINE_SW_H
