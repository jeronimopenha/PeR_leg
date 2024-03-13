#ifndef CPP_STAGE8_SA_HLS_H
#define CPP_STAGE8_SA_HLS_H

#include "types_sa_hls.hpp"

class Stage8SaHls
{
private:
public:
    ST8_OUT new_output = {0, false, 0, 0};
    ST8_OUT old_output = {0, false, 0, 0};

    void compute(ST7_OUT st7_input);
};
#endif
