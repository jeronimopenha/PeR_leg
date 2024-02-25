#include <iostream>

class Stage6SA {
private:
    int* new_output;
    int* old_output;

public:
    Stage6SA() {
        new_output = new int[10]();
        old_output = new int[10]();
    }

    ~Stage6SA() {
        delete[] new_output;
        delete[] old_output;
    }

    void compute(int* st5_input) {
        std::copy(new_output, new_output + 10, old_output);

        int st5_th_idx = st5_input[0];
        bool st5_th_valid = st5_input[1];
        int* st5_dvac = st5_input + 2;
        int* st5_dvbc = st5_input + 4;
        int* st5_dvas = st5_input + 6;
        int* st5_dvbs = st5_input + 10;

        int dvac = st5_dvac[0] + st5_dvac[1];
        int dvbc = st5_dvbc[0] + st5_dvbc[1];
        int dvas[2] = {st5_dvas[0] + st5_dvas[1], st5_dvas[2] + st5_dvas[3]};
        int dvbs[2] = {st5_dvbs[0] + st5_dvbs[1], st5_dvbs[2] + st5_dvbs[3]};

        std::copy(st5_input, st5_input + 10, new_output);
        std::copy(dvac, dvac + 1, new_output + 2);
        std::copy(dvbc, dvbc + 1, new_output + 3);
        std::copy(dvas, dvas + 2, new_output + 4);
        std::copy(dvbs, dvbs + 2, new_output + 6);
    }
};