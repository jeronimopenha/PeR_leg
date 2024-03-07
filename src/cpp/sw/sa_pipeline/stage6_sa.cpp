#include "sa_pipeline_sw.h"

class Stage6SA {
private:


public:
    ST6_OUT new_output = {
            0, false, 0, 0,
            {0, 0},
            {0, 0}
    };
    ST6_OUT old_output = {
            0, false, 0, 0,
            {0, 0},
            {0, 0}
    };

    void compute(ST5_OUT st5_input) {
        this->old_output.th_idx = this->new_output.th_idx;
        this->old_output.th_valid = this->new_output.th_valid;
        this->old_output.dvac = this->new_output.dvac;
        this->old_output.dvbc = this->new_output.dvbc;
        memcpy(&this->old_output.dvas, &this->new_output.dvas, sizeof(this->new_output.dvas));
        memcpy(&this->old_output.dvbs, &this->new_output.dvbs, sizeof(this->new_output.dvbs));

        int st5_th_idx = st5_input.th_idx;
        bool st5_th_valid = st5_input.th_valid;

        if (st5_th_idx == 0 && st5_th_valid) {
            int a = 1;
        }

        int dvac = st5_input.dvac[0] + st5_input.dvac[1];
        int dvbc = st5_input.dvbc[0] + st5_input.dvbc[1];
        int dvas[2] = {st5_input.dvas[0] + st5_input.dvas[1], st5_input.dvas[2] + st5_input.dvas[3]};
        int dvbs[2] = {st5_input.dvbs[0] + st5_input.dvbs[1], st5_input.dvbs[2] + st5_input.dvbs[3]};

        this->new_output.th_idx = st5_th_idx;
        this->new_output.th_valid = st5_th_valid;
        this->new_output.dvac = dvac;
        this->new_output.dvbc = dvbc;
        memcpy(&this->new_output.dvas, &dvas, sizeof(dvas));
        memcpy(&this->new_output.dvbs, &dvbs, sizeof(dvbs));
    }
};