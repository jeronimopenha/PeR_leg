#include <iostream>

class Stage7SA {
private:
    int* new_output;
    int* old_output;

public:
    Stage7SA() {
        new_output = new int[5]();
        old_output = new int[5]();
    }

    ~Stage7SA() {
        delete[] new_output;
        delete[] old_output;
    }

    void compute(int* st6_input) {
        std::copy(new_output, new_output + 5, old_output);

        int st6_th_idx = st6_input[0];
        bool st6_th_valid = st6_input[1];
        int st6_dvac = st6_input[2];
        int st6_dvbc = st6_input[3];
        int* st6_dvas = st6_input + 4;
        int* st6_dvbs = st6_input + 6;

        int dc = st6_dvac + st6_dvbc;
        int dvas = st6_dvas[0] + st6_dvas[1];
        int dvbs = st6_dvbs[0] + st6_dvbs[1];

        std::copy(st6_input, st6_input + 5, new_output);
        new_output[2] = dc;
        new_output[3] = dvas;
        new_output[4] = dvbs;
    }
};