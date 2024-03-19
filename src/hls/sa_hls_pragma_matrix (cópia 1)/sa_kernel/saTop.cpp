
#include "saTop.hpp"

extern "C" void simulatedAnnealingTop(ap_int<8> *n2c, ap_int<8> *c2n, ap_int<8> *n)
{
#pragma HLS INTERFACE m_axi port = n2c offset = slave
#pragma HLS INTERFACE m_axi port = c2n offset = slave
#pragma HLS INTERFACE m_axi port = n offset = slave
#pragma HLS INTERFACE s_axilite port = return

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
            c2n_l[i][] j = c2n[idx];
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
    sa_pipeline_hw.run_single((ap_int<8> *)n2c0_l, (ap_int<8> *)n2c1_l, (ap_int<8> *)n2c2_l, (ap_int<8> *)n2c3_l, (ap_int<8> *)c2n_l, (ap_int<8> *)n0_l, (ap_int<8> *)n1_l, (ap_int<8> *)n2_l, (ap_int<8> *)n3_l);

    // memcpy(n2c, (ap_int<8> *)n2c_l, N_C_N_DATA * sizeof(ap_int<8>));
    memcpy(c2n, (ap_int<8> *)c2n_l, N_C_N_DATA * sizeof(ap_int<8>));
    // memcpy(n, (ap_int<8> *)n_l, N_N_DATA * sizeof(ap_int<8>));

    // for (int i  = 0; i<N_C_N_DATA; i++){
    //     n2c[i] = n2c_l[i];
    //     c2n[i] = c2n_l[i];
    // }
    // for (int i  = 0; i<N_C_N_DATA; i++){
    //     n[i] = n_l[i];
    // }
}
