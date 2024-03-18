#ifndef CPP_STAGE2_SA_HLS_H
#define CPP_STAGE2_SA_HLS_H

#include "types_sa_hls.hpp"

class Stage2SaHls
{
private:
public:
    ST2_OUT m_new_output = {0, false, 0, 0, 0, 0, {-1, -1, -1, -1}, {-1, -1, -1, -1}, {0, false, false}, {0, 0, -1}, {0, 0, -1}};
    ST2_OUT m_old_output = {0, false, 0, 0, 0, 0, {-1, -1, -1, -1}, {-1, -1, -1, -1}, {0, false, false}, {0, 0, -1}, {0, 0, -1}};

    void compute(ST1_OUT st1_input, ap_int<8> *neighbors0, ap_int<8> *neighbors1, ap_int<8> *neighbors2, ap_int<8> *neighbors3);
};
#endif
