#ifndef CPP_STAGE3_SA_HLS_H
#define CPP_STAGE3_SA_HLS_H

#include "types_sa_hls.hpp"

class Stage3SaHls
{
private:
    bool flag;

public:
    ST3_OUT new_output = {0, false, 0, 0, {-1, -1, -1, -1}, {-1, -1, -1, -1}, {0, false, false}, {0, 0, -1}, {0, 0, -1}};
    ST3_OUT old_output = {0, false, 0, 0, {-1, -1, -1, -1}, {-1, -1, -1, -1}, {0, false, false}, {0, 0, -1}, {0, 0, -1}};

    Stage3SaHls();
    void compute(ST2_OUT st2_input, W st3_wb, int (&n2c)[N_THREADS][N_CELLS]);
};
#endif
