#include <iostream>

class Stage1SA {
private:
    int** c2n;
    int n_threads;
    bool flag;
    int* new_output;
    int* old_output;
    struct FIFO {
        int th_idx;
        int cell;
        int node;
    };
    FIFO* fifo_a;
    FIFO* fifo_b;

public:
    Stage1SA(int** c2n, int n_threads) :
        n_threads(n_threads),
        flag(true)
    {
        this->c2n = c2n;
        new_output = new int[9]();
        old_output = new int[9]();
        fifo_a = new FIFO[n_threads - 2]();
        fifo_b = new FIFO[n_threads - 2]();
    }

    ~Stage1SA() {
        delete[] new_output;
        delete[] old_output;
        delete[] fifo_a;
        delete[] fifo_b;
    }

    void compute(int* st0_input, int* st9_sw, int* st1_wb) {
        std::copy(new_output, new_output + 9, old_output);

        int st0_th_idx = st0_input[0];
        bool st0_th_valid = st0_input[1];
        int st0_cell_a = st0_input[2];
        int st0_cell_b = st0_input[3];

        if (st0_th_valid) {
            fifo_a[n_threads - 2] = {new_output[0], new_output[2], old_output[7]};
            fifo_b[n_threads - 2] = {new_output[0], new_output[3], new_output[6]};
        }

        FIFO wa = {new_output[7], new_output[4], new_output[5]};
        FIFO wb = {new_output[6], new_output[8], st1_wb[2]};
        if (st0_th_valid) {
            wa = fifo_a[0];
            wb = fifo_b[0];
        }

        bool usw = st9_sw[2];
        FIFO uwa = {new_output[4], new_output[5], new_output[6]};
        FIFO uwb = {st1_wb[0], st1_wb[1], st1_wb[2]};
        if (usw) {
            if (flag) {
                c2n[uwa.th_idx][uwa.cell] = wa.node;
                flag = !flag;
            } else {
                c2n[uwb.th_idx][uwb.cell] = uwb.node;
                flag = !flag;
                if (uwb.th_idx == 0) {
                    // Pass, or you can print matrix here if needed
                }
            }
        }

        new_output[0] = st0_th_idx;
        new_output[1] = st0_th_valid;
        new_output[2] = st0_cell_a;
        new_output[3] = st0_cell_b;
        new_output[4] = c2n[st0_th_idx][st0_cell_a];
        new_output[5] = c2n[st0_th_idx][st0_cell_b];
        new_output[6] = wb.th_idx;
        new_output[7] = wa.th_idx;
        new_output[8] = wb.cell;
    }
};