
#include "saTop.hpp"

extern "C" void simulatedAnnealingTop(ap_int<8> *n2c, ap_int<8> *c2n, ap_int<8> *n)
{

    ap_int<8> n2c0_l[N_THREADS][N_CELLS];
    ap_int<8> n2c1_l[N_THREADS][N_CELLS];
    ap_int<8> n2c2_l[N_THREADS][N_CELLS];
    ap_int<8> n2c3_l[N_THREADS][N_CELLS];
    ap_int<8> c2n_l[N_THREADS][N_CELLS];
    ap_int<8> n0_l[N_CELLS][N_NEIGH];
    ap_int<8> n1_l[N_CELLS][N_NEIGH];
    ap_int<8> n2_l[N_CELLS][N_NEIGH];
    ap_int<8> n3_l[N_CELLS][N_NEIGH];

    for (ap_int<8> i = 0; i < N_THREADS; i++)
    {
        for (ap_int<8> j = 0; j < N_CELLS)
        {
            ap_int<8> idx = i * N_THREADS + j;
            n2c0_l[i][j] = n2c[idx];
            n2c0_l[i][j] = n2c[idx];
            n2c0_l[i][j] = n2c[idx];
            n2c0_l[i][j] = n2c[idx];
            c2n_l[i][j] = c2n[idx];
        }
    }
    for (ap_int<8> i = 0; i < N_CELLS; i++)
    {
        for (ap_int<8> j = 0; j < N_NEIGH)
        {
            ap_int<8> idx = i * N_CELLS + j;
            n_l[i[j]] = n[idx];
        }
    }

    static PipelineSaHls sa_pipeline_hw;
    sa_pipeline_hw.exec_pipeline(
        (ap_int<8> **)n2c0_l,
        (ap_int<8> **)n2c1_l,
        (ap_int<8> **)n2c2_l,
        (ap_int<8> **)n2c3_l,
        (ap_int<8> **)c2n_l,
        (ap_int<8> **)n0_l,
        (ap_int<8> **)n1_l,
        (ap_int<8> **)n2_l,
        (ap_int<8> **)n3_l);

    for (ap_int<8> i = 0; i < N_THREADS; i++)
    {
        for (ap_int<8> j = 0; j < N_CELLS)
        {
            ap_int<8> idx = i * N_THREADS + j;
            c2n[idx] = c2n_l[i][j];
        }
    }
}
