//
// Created by jeronimo on 04/03/24.
//

#ifndef CPP_SA_DEFS_H
#define CPP_SA_DEFS_H

#define N_NEIGH 4
#define N_THREADS 6

/*struct SW {
    int th_idx;
    char th_valid;
    char sw;
} SW_DEFAULT = {
        0,
        0,
        0
};

struct W {
    int th_idx;
    int cell;
    int node;
} W_DEFAULT = {
        0,
        0,
        0
};

struct ST0_OUT {
    int th_idx;
    char th_valid;
    int cell_a;
    int cell_b;
} ST0_OUT_DEFAULT = {
        0,
        0,
        0, 0
};

struct ST1_OUT {
    int th_idx;
    char th_valid;
    int cell_a;
    int cell_b;
    int node_a;
    int node_b;
    SW sw;
    W wa;
    W wb;
} ST1_OUT_DEFAULT = {
        0,
        0,
        0,
        0,
        0, 0, {0, 0, 0}
};

struct ST2_OUT {
    int th_idx;
    char th_valid;
    int cell_a;
    int cell_b;
    int node_a;
    int node_b;
    int va[N_NEIGH];
    int vb[N_NEIGH];
    SW sw;
    W wa;
    W wb;
} ST2_OUT_DEFAULT = {
        0,
        0, 0, 0, 0, 0, {-((int) 1), -((int) 1)}, {-((int) 1), -((int) 1)}
};
struct ST3_OUT {
    int th_idx;
    char th_valid;
    int cell_a;
    int cell_b;
    int cva[N_NEIGH];
    int cvb[N_NEIGH];
    SW sw;
    W wa;
    W wb;
};

struct ST4_OUT {
    int th_idx;
    char th_valid;
    int cell_a;
    int cell_b;
    int cva[N_NEIGH];
    int cvb[N_NEIGH];
    int dvac[N_NEIGH];
    int dvbc[N_NEIGH];
};

struct ST5_OUT {
    int th_idx;
    char th_valid;
    int dvac[N_NEIGH / 2];
    int dvbc[N_NEIGH / 2];
    int dvas[N_NEIGH];
    int dvbs[N_NEIGH];
} ST5_OUT_DEFAULT = {
        0,
        0,
        {-((int) 1), -((int) 1)},
        {-((int) 1), -((int) 1)},
        {-((int) 1), -((int) 1), -((int) 1), -((int) 1)},
        {-((int) 1), -((int) 1), -((int) 1), -((int) 1)},
};

struct ST6_OUT {
    int th_idx;
    char th_valid;
    int dvac;
    int dvbc;
    int dvas[N_NEIGH / 2];
    int dvbs[N_NEIGH / 2];
} ST6_OUT_DEFAULT = {
        0,
        0,
        0,
        0,
        {-((int) 1), -((int) 1)},
        {-((int) 1), -((int) 1)},
};

struct ST7_OUT {
    int th_idx;
    char th_valid;
    int dc;
    int dvas;
    int dvbs;
} ST7_OUT_DEFAULT = {
        0, 0, 0, 0, 0};

struct ST8_OUT {
    int th_idx;
    char th_valid;
    int dc;
    int ds;
} ST8_OUT_DEFAULT = {
        0, 0, 0, 0};

struct ST9_OUT {
    int th_idx;
    char th_valid;
    char sw;
} ST9_OUT_DEFAULT = {
        0, 0, 0};*/
#endif //CPP_SA_DEFS_H
