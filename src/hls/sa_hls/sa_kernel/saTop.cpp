
#include "saTop.hpp"

extern "C" void simulatedAnnealingTop(ap_int<8> *n2c, ap_int<8> *c2n, ap_int<8> *n)
{
#pragma HLS INTERFACE m_axi port = n2c offset = slave
#pragma HLS INTERFACE m_axi port = c2n offset = slave
#pragma HLS INTERFACE m_axi port = n offset = slave
#pragma HLS INTERFACE s_axilite port = return

    ap_int<8> n2c_l[N_C_N_DATA];
    ap_int<8> c2n_l[N_C_N_DATA];
    ap_int<8> n_l[N_N_DATA];

    // for (int i  = 0; i<N_C_N_DATA; i++){
    //     n2c_l[i] = n2c[i];
    //     c2n_l[i] = c2n[i];
    // }
    // for (int i  = 0; i<N_C_N_DATA; i++){
    //     n_l[i] = n[i];
    // }

    memcpy((ap_int<8> *)n2c_l, n2c, N_C_N_DATA * sizeof(ap_int<8>));
    memcpy((ap_int<8> *)c2n_l, c2n, N_C_N_DATA * sizeof(ap_int<8>));
    memcpy((ap_int<8> *)n_l, n, N_N_DATA * sizeof(ap_int<8>));

    static PipelineSaHls sa_pipeline_hw;
    sa_pipeline_hw.run_single((ap_int<8> *)n2c_l, (ap_int<8> *)c2n_l, (ap_int<8> *)n_l);

    memcpy(n2c, (ap_int<8> *)n2c_l, N_C_N_DATA * sizeof(ap_int<8>));
    memcpy(c2n, (ap_int<8> *)c2n_l, N_C_N_DATA * sizeof(ap_int<8>));
    memcpy(n, (ap_int<8> *)n_l, N_N_DATA * sizeof(ap_int<8>));

    // for (int i  = 0; i<N_C_N_DATA; i++){
    //     n2c[i] = n2c_l[i];
    //     c2n[i] = c2n_l[i];
    // }
    // for (int i  = 0; i<N_C_N_DATA; i++){
    //     n[i] = n_l[i];
    // }
}
