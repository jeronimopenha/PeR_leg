#include <iostream>

class Stage8SA {
private:
    int* new_output;
    int* old_output;

public:
    Stage8SA() {
        new_output = new int[4]();
        old_output = new int[4]();
    }

    ~Stage8SA() {
        delete[] new_output;
        delete[] old_output;
    }

    void compute(int* st7_input) {
        std::copy(new_output, new_output + 4, old_output);

        int st7_th_idx = st7_input[0];
        bool st7_th_valid = st7_input[1];
        int st7_dc = st7_input[2];

        // fixme only for debugging
        // if st7_th_idx == 0:
        //    z = 1

        int st7_dvas = st7_input[3];
        int st7_dvbs = st7_input[4];

        int ds = st7_dvas + st7_dvbs;

        std::copy(st7_input, st7_input + 4, new_output);
        new_output[2] = st7_dc;
        new_output[3] = ds;
    }
};