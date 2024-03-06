#include "sa_pipeline_sw.h"
#include "fifo_sa.cpp"

class Stage1SA {
private:
    bool flag;

    FifoSa<W> *fifo_a;
    FifoSa<W> *fifo_b;

public:
    ST1_OUT new_output = {
            0, false, 0, 0, 0, 0,
            {0, false, false},
            {0, 0, 0},
            {0, 0, 0}
    };
    ST1_OUT old_output = {
            0, false, 0, 0, 0, 0,
            {0, false, false},
            {0, 0, 0},
            {0, 0, 0}
    };

    explicit Stage1SA() {
        this->flag = true;
        this->fifo_a = new FifoSa<W>(N_THREADS);
        this->fifo_b = new FifoSa<W>(N_THREADS);
        for (int i = 0; i < N_THREADS - 2; i++) {
            W fifo_cell_a = {0, 0, -1};
            W fifo_cell_b = {0, 0, -1};
            this->fifo_a->enqueue(fifo_cell_a);
            this->fifo_b->enqueue(fifo_cell_b);
        }
    }

    ~Stage1SA() {
        delete[] fifo_a;
        delete[] fifo_b;
    }


    void compute(ST0_OUT st0_input, ST9_OUT st9_sw, W st1_wb, int (&c2n)[N_THREADS][N_CELLS]) {
        this->old_output.th_idx = this->new_output.th_idx;
        this->old_output.th_valid = this->new_output.th_valid;
        this->old_output.cell_a = this->new_output.cell_a;
        this->old_output.cell_b = this->new_output.cell_b;
        this->old_output.node_a = this->new_output.node_a;
        this->old_output.node_b = this->new_output.node_b;
        memcpy(&this->old_output.sw, &this->new_output.sw, sizeof(ST9_OUT));
        memcpy(&this->old_output.wa, &this->new_output.wa, sizeof(W));
        memcpy(&this->old_output.wb, &this->new_output.wb, sizeof(W));

        int st0_th_idx = st0_input.th_idx;
        bool st0_th_valid = st0_input.th_valid;
        int st0_cell_a = st0_input.cell_a;
        int st0_cell_b = st0_input.cell_b;

        if(st0_th_idx ==0 && st0_th_valid){
            int a=1;
        }

        if (st0_th_valid) {
            this->fifo_a->enqueue(W{this->new_output.th_idx, this->new_output.cell_a, this->new_output.node_b});
            this->fifo_b->enqueue(W{this->new_output.th_idx, this->new_output.cell_b, this->new_output.node_a});
        }

        W wa{};
        W wb{};
        if (st0_th_valid) {
            wa = this->fifo_a->dequeue();
            wb = this->fifo_b->dequeue();
        } else {
            memcpy(&wa, &this->new_output.wa, sizeof(W));
            memcpy(&wb, &this->new_output.wb, sizeof(W));
        }

        bool usw = st9_sw.sw;
        W uwa{};
        W uwb{};
        memcpy(&uwa, &this->new_output.wa, sizeof(W));
        memcpy(&uwb, &st1_wb, sizeof(W));
        if (usw) {
            if (this->flag) {
                c2n[uwa.th_idx][uwa.cell] = wa.node;
                this->flag = !this->flag;
            } else {
                c2n[uwb.th_idx][uwb.cell] = uwb.node;
                this->flag = !this->flag;
            }
        }

        this->new_output.th_idx = st0_th_idx;
        this->new_output.th_valid = st0_th_valid;
        this->new_output.cell_a = st0_cell_a;
        this->new_output.cell_b = st0_cell_b;
        this->new_output.node_a = c2n[st0_th_idx][st0_cell_a];
        this->new_output.node_b = c2n[st0_th_idx][st0_cell_b];
        memcpy(&this->new_output.sw, &st9_sw, sizeof(ST9_OUT));
        memcpy(&this->new_output.wa, &wa, sizeof(W));
        memcpy(&this->new_output.wb, &wb, sizeof(W));
    }
};