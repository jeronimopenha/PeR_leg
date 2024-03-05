#include <cstring>
#include "sa_pipeline_sw.h"

class Stage2SA {
private:
    int **neighbors;


public:
    ST2_OUT new_output = {
            0, false, 0, 0, 0, 0,
            {-1, -1, -1, -1},
            {-1, -1, -1, -1},
            {0, false, false},
            {0, 0, -1},
            {0, 0, -1}
    };
    ST2_OUT old_output = {
            0, false, 0, 0, 0, 0,
            {-1, -1, -1, -1},
            {-1, -1, -1, -1},
            {0, false, false},
            {0, 0, -1},
            {0, 0, -1}
    };

    explicit Stage2SA(int **neighbors) {
        this->neighbors = neighbors;
    }


    void compute(ST1_OUT st1_input) {

        this->old_output.th_idx = this->new_output.th_idx;
        this->old_output.th_valid = this->new_output.th_valid;
        this->old_output.cell_a = this->new_output.cell_a;
        this->old_output.cell_b = this->new_output.cell_b;
        this->old_output.node_a = this->new_output.node_a;
        this->old_output.node_b = this->new_output.node_b;
        memcpy(&this->old_output.va, &this->new_output.va, sizeof(this->new_output.va));
        memcpy(&this->old_output.vb, &this->new_output.vb, sizeof(this->new_output.vb));
        memcpy(&this->old_output.sw, &this->new_output.sw, sizeof(ST9_OUT));
        memcpy(&this->old_output.wa, &this->new_output.wa, sizeof(W));
        memcpy(&this->old_output.wb, &this->new_output.wb, sizeof(W));

        int st1_th_idx = st1_input.th_idx;
        bool st1_th_valid = st1_input.th_valid;
        int st1_cell_a = st1_input.cell_a;
        int st1_cell_b = st1_input.cell_b;
        int st1_node_a = st1_input.node_a;
        int st1_node_b = st1_input.node_b;
        ST9_OUT st1_sw{};
        W st1_wa{};
        W st1_wb{};
        memcpy(&st1_sw, &st1_input.sw, sizeof(ST9_OUT));
        memcpy(&st1_wa, &st1_input.wa, sizeof(W));
        memcpy(&st1_wb, &st1_input.wa, sizeof(W));

        int va[N_NEIGH] = {-1, -1, -1, -1};
        int vb[N_NEIGH] = {-1, -1, -1, -1};


        if (st1_node_a != -1) {
            for (int n = 0; n < N_NEIGH; ++n) {
                va[n] = neighbors[st1_node_a][n];
            }
        }
        if (st1_node_b != -1) {
            for (int n = 0; n < 4; ++n) {
                vb[n] = neighbors[st1_node_b][n];
            }
        }
        this->new_output.th_idx = st1_th_idx;
        this->new_output.th_valid = st1_th_valid;
        this->new_output.cell_a = st1_cell_a;
        this->new_output.cell_b = st1_cell_b;
        this->new_output.node_a = st1_node_a;
        this->new_output.node_b = st1_node_b;
        memcpy(&this->new_output.va, &va, sizeof(va));
        memcpy(&this->new_output.vb, &vb, sizeof(vb));
        memcpy(&this->new_output.sw, &st1_sw, sizeof(ST9_OUT));
        memcpy(&this->new_output.wa, &st1_wa, sizeof(W));
        memcpy(&this->new_output.wb, &st1_wb, sizeof(W));
    }
};