#include "stage1_sa.h"
#include "fifo_sa.cpp"

class Stage1SA {
private:
    int **c2n;
    bool flag;
    ST1_OUT new_output = {
            0, false, 0, 0, 0, 0,
            {int(0), bool(false), bool(false)},
            {int(0), int(0), int(0)},
            {int(0), int(0), int(0)}
    };
    ST1_OUT old_output = {
            0, false, 0, 0, 0, 0,
            {int(0), bool(false), bool(false)},
            {int(0), int(0), int(0)},
            {int(0), int(0), int(0)}
    };

    FifoSa<W> *fifo_a;
    FifoSa<W> *fifo_b;

public:
    explicit Stage1SA(int **c2n) {
        this->c2n = c2n;
        this->flag = false;
        this->fifo_a = new FifoSa<W>(N_THREADS);
        this->fifo_b = new FifoSa<W>(N_THREADS);
        for (int i = 0; i < N_THREADS - 2; i++) {
            W fifo_cell_a = {0, 0, 0};
            W fifo_cell_b = {0, 0, 0};
            this->fifo_a->enqueue(fifo_cell_a);
            this->fifo_b->enqueue(fifo_cell_b);
        }
    }

    ~Stage1SA() {
        delete[] fifo_a;
        delete[] fifo_b;
    }


    void compute(ST0_OUT st0_input, SW st9_sw, W st1_wb) {
        this->old_output.th_idx = this->new_output.th_idx;
        this->old_output.th_valid = this->new_output.th_valid;
        this->old_output.cell_a = this->new_output.cell_a;
        this->old_output.cell_b = this->new_output.cell_b;
        this->old_output.node_a = this->new_output.node_a;
        this->old_output.node_b = this->new_output.node_b;
        this->old_output.sw.th_idx = this->new_output.sw.th_idx;
        this->old_output.sw.th_valid = this->new_output.sw.th_valid;
        this->old_output.sw.sw = this->new_output.sw.sw;
        this->old_output.wa.th_idx = this->new_output.wa.th_idx;
        this->old_output.wa.cell = this->new_output.wa.cell;
        this->old_output.wa.node = this->new_output.wa.node;
        this->old_output.wb.th_idx = this->new_output.wb.th_idx;
        this->old_output.wb.cell = this->new_output.wb.cell;
        this->old_output.wb.node = this->new_output.wb.node;

        int st0_th_idx = st0_input.th_idx;
        bool st0_th_valid = st0_input.th_valid;
        int st0_cell_a = st0_input.cell_a;
        int st0_cell_b = st0_input.cell_b;

        if (st0_th_valid) {
            this->fifo_a->enqueue(W{this->new_output.th_idx, this->new_output.cell_a, this->new_output.node_b});
            this->fifo_b->enqueue(W{this->new_output.th_idx, this->new_output.cell_b, this->new_output.node_a});
        }

        W wa{};
        W wb{};
        if (st0_th_valid) {
            wa = fifo_a->dequeue();
            wb = fifo_b->dequeue();
        } else {
            wa = this->new_output.wa;
            wb = this->new_output.wb;
        }

        bool usw = st9_sw[2];
        FIFO_ST uwa = {new_output[4], new_output[5], new_output[6]};
        FIFO_ST uwb = {st1_wb[0], st1_wb[1], st1_wb[2]};
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

        new_output.th_idx = st0_th_idx;
        new_output.th_valid = st0_th_valid;
        new_output.cell_a = st0_cell_a;
        new_output.cell_b = st0_cell_b;
        new_output.node_a = c2n[st0_th_idx][st0_cell_a];
        new_output.node_b = c2n[st0_th_idx][st0_cell_b];
        new_output[6] = wb.th_idx;
        new_output[7] = wa.th_idx;
        new_output[8] = wb.cell;
    }
};