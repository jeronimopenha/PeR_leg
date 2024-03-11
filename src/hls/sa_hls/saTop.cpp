
#include <saTop.hpp>

extern "C" void simulatedAnnealingTop(int ***n2c,int ***c2n,int **n){
#pragma HLS INTERFACE m_axi port = mem1 offset = slave
#pragma HLS INTERFACE m_axi port = mem2 offset = slave
#pragma HLS INTERFACE m_axi port = mem3 offset = slave
#pragma HLS INTERFACE s_axilite port = return

    static SAPipelineHls sa_pipeline_hw;
    sa_pipeline_hw.run_single(n2c,c2n,n);

}
