
#include "saTop.hpp"

extern "C" void simulatedAnnealingTop(int *n2c,int *c2n,int *n){
#pragma HLS INTERFACE m_axi port = n2c offset = slave
#pragma HLS INTERFACE m_axi port = c2n offset = slave
#pragma HLS INTERFACE m_axi port = n   offset = slave
#pragma HLS INTERFACE s_axilite port = return

    int n2c_l[N_C_N_DATA];
    int c2n_l[N_C_N_DATA];
    int n_l[N_N_DATA];
    
    // for (int i  = 0; i<N_C_N_DATA; i++){
    //     n2c_l[i] = n2c[i];
    //     c2n_l[i] = c2n[i];
    // }
    // for (int i  = 0; i<N_C_N_DATA; i++){
    //     n_l[i] = n[i];
    // }
    
    memcpy((int *) n2c_l, n2c , N_C_N_DATA * sizeof(int));
    memcpy((int *) c2n_l, c2n , N_C_N_DATA * sizeof(int));
    memcpy((int *) n_l, n , N_N_DATA * sizeof(int));
    
    static PipelineSaHls sa_pipeline_hw;
    sa_pipeline_hw.run_single((int *) n2c_l,(int *) c2n_l,(int *) n_l);
    
    memcpy(n2c, (int *) n2c_l, N_C_N_DATA * sizeof(int));
    memcpy(c2n, (int *) c2n_l, N_C_N_DATA * sizeof(int));
    memcpy(n, (int *) n_l, N_N_DATA * sizeof(int));
    
    // for (int i  = 0; i<N_C_N_DATA; i++){
    //     n2c[i] = n2c_l[i];
    //     c2n[i] = c2n_l[i];
    // }
    // for (int i  = 0; i<N_C_N_DATA; i++){
    //     n[i] = n_l[i];
    // }

}
