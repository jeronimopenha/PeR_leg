#ifndef CPP_STAGE1_SA_HLS_H
#define CPP_STAGE1_SA_HLS_H

#include "fifo_sa_hls.hpp"

class Stage1SaHls
{
private:
    bool flag;

    FifoSaHls *fifo_a;
    FifoSaHls *fifo_b;

public:
    ST1_OUT new_output = {0, false, 0, 0, 0, 0, {0, false, false}, {0, 0, 0}, {0, 0, 0}};
    ST1_OUT old_output = {0, false, 0, 0, 0, 0, {0, false, false}, {0, 0, 0}, {0, 0, 0}};

    Stage1SaHls();
    void compute(ST0_OUT st0_input, ST9_OUT st9_sw, W st1_wb, int (&c2n)[N_THREADS][N_CELLS]);
};
#endif