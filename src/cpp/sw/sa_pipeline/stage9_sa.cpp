#include <iostream>

class Stage9SA {
private:
    bool sw;
    int* new_output;
    int* old_output;

public:
    Stage9SA() {
        new_output = new int[3]();
        old_output = new int[3]();
    }

    ~Stage9SA() {
        delete[] new_output;
        delete[] old_output;
    }

    void compute(int* st8_input) {
        std::copy(new_output, new_output + 3, old_output);

        int st8_th_idx = st8_input[0];
        bool st8_th_valid = st8_input[1];
        int st8_dc = st8_input[2];
        int st8_ds = st8_input[3];

        bool sw = st8_ds < st8_dc;

        std::copy(st8_input, st8_input + 3, new_output);
        new_output[2] = sw;
    }
};