#include <iostream>

class Stage2SA {
private:
    int** neighbors;
    int* new_output;
    int* old_output;

public:
    Stage2SA(int** neighbors) {
        this->neighbors = neighbors;
        new_output = new int[15]();
        old_output = new int[15]();
    }

    ~Stage2SA() {
        delete[] new_output;
        delete[] old_output;
    }

    void compute(int* st1_input) {
        std::copy(new_output, new_output + 15, old_output);

        int st1_th_idx = st1_input[0];
        bool st1_th_valid = st1_input[1];
        int st1_cell_a = st1_input[2];
        int st1_cell_b = st1_input[3];
        int st1_node_a = st1_input[4];
        int st1_node_b = st1_input[5];
        bool st1_sw = st1_input[6];
        int* st1_va = st1_input + 7;
        int* st1_vb = st1_input + 11;

        int va[4] = {-1, -1, -1, -1};
        int vb[4] = {-1, -1, -1, -1};

        if (st1_node_a != -1) {
            for (int i = 0; i < 4; ++i) {
                va[i] = neighbors[st1_node_a][i];
            }
        }
        if (st1_node_b != -1) {
            for (int i = 0; i < 4; ++i) {
                vb[i] = neighbors[st1_node_b][i];
            }
        }

        std::copy(st1_input, st1_input + 15, new_output);
        std::copy(va, va + 4, new_output + 7);
        std::copy(vb, vb + 4, new_output + 11);
    }
};