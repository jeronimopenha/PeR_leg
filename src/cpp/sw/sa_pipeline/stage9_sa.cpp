#include "sa_pipeline_sw.h"

class Stage9SA {
private:
    bool sw;


public:
    ST9_OUT new_output = {0, false, false};
    ST9_OUT old_output = {0, false, false};

    Stage9SA() {
        this->sw = false;
    }

    void compute(ST8_OUT st8_input) {
        this->old_output.th_idx = this->new_output.th_idx;
        this->old_output.th_valid = this->new_output.th_valid;
        this->old_output.sw = this->new_output.sw;

        int st8_th_idx = st8_input.th_idx;
        bool st8_th_valid = st8_input.th_valid;
        int st8_dc = st8_input.dc;
        int st8_ds = st8_input.ds;

        bool sw_c = st8_ds < st8_dc;

        this->new_output.th_idx = st8_th_idx;
        this->new_output.th_valid = st8_th_valid;
        this->new_output.sw = sw_c;
    }
};