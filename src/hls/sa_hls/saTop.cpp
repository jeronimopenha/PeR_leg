
#include "saTop.hpp"

extern "C" void simulatedAnnealingTop(int *n2c,int *c2n,int *n){
#pragma HLS INTERFACE m_axi port = n2c offset = slave
#pragma HLS INTERFACE m_axi port = c2n offset = slave
#pragma HLS INTERFACE m_axi port = n   offset = slave
#pragma HLS INTERFACE s_axilite port = return

    static PipelineSaHls sa_pipeline_hw;
    sa_pipeline_hw.run_single(n2c,c2n,n);

}
