#include <iostream>

class Stage3SA {
private:
    int** n2c;
    int* new_output;
    int* old_output;
    bool flag;

public:
    Stage3SA(int** n2c, int n_threads) :
        n_threads(n_threads),
        flag(true)
    {
        this->n2c = n2c;
        new_output = new int[14]();
        old_output = new int[14]();
    }

    ~Stage3SA() {
        delete[] new_output;
        delete[] old_output;
    }

    void compute(int* st2_input, int* st3_wb) {
        std::copy(new_output, new_output + 14, old_output);

        int st2_th_idx = st2_input[0];
        bool st2_th_valid = st2_input[1];
        int st2_cell_a = st2_input[2];
        int st2_cell_b = st2_input[3];
        bool st2_sw = st2_input[4];
        int* st2_va = st2_input + 5;
        int* st2_vb = st2_input + 9;
        int* st2_wa = st2_input + 13;
        int* st2_wb = st3_wb;

        bool usw = old_output[10];
        int* uwa = old_output + 11;
        int* uwb = st3_wb;
        if (usw) {
            if (flag) {
                if (uwa[2] != -1) {
                    n2c[uwa[0]][uwa[2]] = uwa[1];
                }
                flag = !flag;
            } else {
                if (uwb[2] != -1) {
                    n2c[uwb[0]][uwb[2]] = uwb[1];
                }
                flag = !flag;
            }
        }

        int cva[4] = {-1, -1, -1, -1};
        int cvb[4] = {-1, -1, -1, -1};

        for (int i = 0; i < 4; ++i) {
            if (st2_va[i] != -1) {
                cva[i] = n2c[st2_th_idx][st2_va[i]];
            }
            if (st2_vb[i] != -1) {
                cvb[i] = n2c[st2_th_idx][st2_vb[i]];
            }
        }

        std::copy(st2_input, st2_input + 14, new_output);
        std::copy(cva, cva + 4, new_output + 6);
        std::copy(cvb, cvb + 4, new_output + 10);
    }
};