#include "sa_pipeline_sw.h"

class Stage3SA {
private:
    bool flag;

public:

    ST3_OUT new_output = {
            0, false, 0, 0,
            {-1, -1, -1, -1},
            {-1, -1, -1, -1},
            {0, false, false},
            {0, 0, -1},
            {0, 0, -1}
    };
    ST3_OUT old_output = {
            0, false, 0, 0,
            {-1, -1, -1, -1},
            {-1, -1, -1, -1},
            {0, false, false},
            {0, 0, -1},
            {0, 0, -1}
    };

    explicit Stage3SA() {
        this->flag = true;
    }


    void compute(ST2_OUT st2_input, W st3_wb, int (&n2c)[N_THREADS][N_CELLS]) {
        this->old_output.th_idx = this->new_output.th_idx;
        this->old_output.th_valid = this->new_output.th_valid;
        this->old_output.cell_a = this->new_output.cell_a;
        this->old_output.cell_b = this->new_output.cell_b;
        memcpy(&this->old_output.cva, &this->new_output.cva, sizeof(this->new_output.cva));
        memcpy(&this->old_output.cvb, &this->new_output.cvb, sizeof(this->new_output.cvb));
        memcpy(&this->old_output.sw, &this->new_output.sw, sizeof(ST9_OUT));
        memcpy(&this->old_output.wa, &this->new_output.wa, sizeof(W));
        memcpy(&this->old_output.wb, &this->new_output.wb, sizeof(W));

        int st2_th_idx = st2_input.th_idx;
        bool st2_th_valid = st2_input.th_valid;
        int st2_cell_a = st2_input.cell_a;
        int st2_cell_b = st2_input.cell_b;
        int *st2_va = st2_input.va;
        int *st2_vb = st2_input.vb;
        ST9_OUT st2_sw{};
        W st2_wa{};
        W st2_wb{};
        memcpy(&st2_sw, &st2_input.sw, sizeof(ST9_OUT));
        memcpy(&st2_wa, &st2_input.wa, sizeof(W));
        memcpy(&st2_wb, &st2_input.wb, sizeof(W));

        bool usw = old_output.sw.sw;
        W uwa{};
        W uwb{};
        memcpy(&uwa, &this->old_output.wa, sizeof(W));
        memcpy(&uwb, &st3_wb, sizeof(W));

        if (usw) {
            if (flag) {
                if (uwa.node != -1) {
                    n2c[uwa.th_idx][uwa.node] = uwa.cell;
                }
                flag = !flag;
            } else {
                if (uwb.node != -1) {
                    n2c[uwb.th_idx][uwb.node] = uwb.cell;
                }
                flag = !flag;
            }
        }

        int cva[N_NEIGH] = {-1, -1, -1, -1};
        int cvb[N_NEIGH] = {-1, -1, -1, -1};

        for (int n = 0; n < N_NEIGH; ++n) {
            if (st2_va[n] != -1) {
                cva[n] = n2c[st2_th_idx][st2_va[n]];
            }
            if (st2_vb[n] != -1) {
                cvb[n] = n2c[st2_th_idx][st2_vb[n]];
            }
        }

        this->new_output.th_idx = st2_th_idx;
        this->new_output.th_valid = st2_th_valid;
        this->new_output.cell_a = st2_cell_a;
        this->new_output.cell_b = st2_cell_b;
        memcpy(&this->new_output, &cva, sizeof(cva));
        memcpy(&this->new_output, &cvb, sizeof(cvb));
        memcpy(&this->new_output, &st2_sw, sizeof(ST9_OUT));
        memcpy(&this->new_output, &st2_wa, sizeof(W));
        memcpy(&this->new_output, &st2_wb, sizeof(W));
    }
};