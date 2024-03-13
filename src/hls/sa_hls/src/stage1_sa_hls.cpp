#include "stage1_sa_hls.hpp"

Stage1SaHls::Stage1SaHls()
{
    this->flag = true;
    this->fifo_a = new FifoSaHls();
    this->fifo_b = new FifoSaHls();
    for (int i = 0; i < N_THREADS - 2; i++)
    {
        W fifo_cell_a = {0, 0, -1};
        W fifo_cell_b = {0, 0, -1};
        this->fifo_a->enqueue(fifo_cell_a);
        this->fifo_b->enqueue(fifo_cell_b);
    }
    for (int i = 0; i < N_THREADS; i++)
    {
        this->th_idx_offset[i] = i * N_CELLS_SQRT;
    }
}

void Stage1SaHls::compute(ST0_OUT st0_input, ST9_OUT st9_sw, W st1_wb, int *c2n, int exec_offset)
{
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

    if (st0_th_idx == 0 && st0_th_valid)
    {
        int a = 1;
    }

    if (st0_th_valid)
    {
        this->fifo_a->enqueue(W{this->new_output.th_idx, this->new_output.cell_a, this->new_output.node_b});
        this->fifo_b->enqueue(W{this->new_output.th_idx, this->new_output.cell_b, this->new_output.node_a});
    }

    W wa{};
    W wb{};
    if (st0_th_valid)
    {
        wa = this->fifo_a->dequeue();
        wb = this->fifo_b->dequeue();
    }
    else
    {
        wa.th_idx = this->new_output.wa.th_idx;
        wa.cell = this->new_output.wa.cell;
        wa.node = this->new_output.wa.node;
        wb.th_idx = this->new_output.wb.th_idx;
        wb.cell = this->new_output.wb.cell;
        wb.node = this->new_output.wb.node;
    }

    bool usw = this->new_output.sw.sw;
    W uwa{};
    W uwb{};
    uwa.th_idx = this->new_output.wa.th_idx;
    uwa.cell = this->new_output.wa.cell;
    uwa.node = this->new_output.wa.node;
    uwb.th_idx = st1_wb.th_idx;
    uwb.cell = st1_wb.cell;
    uwb.node = st1_wb.node;

    if (usw)
    {
        if (this->flag)
        {
            int idx = exec_offset + this->th_idx_offset[uwa.th_idx] + uwa.cell;
            c2n[idx] = wa.node;
            this->flag = !this->flag;
        }
        else
        {
            int idx = exec_offset + this->th_idx_offset[uwb.th_idx] + uwb.cell;
            c2n[idx] = uwb.node;
            this->flag = !this->flag;
        }
    }
    int idxa = exec_offset + this->th_idx_offset[st0_th_idx] + st0_cell_a;
    int idxb = exec_offset + this->th_idx_offset[st0_th_idx] + st0_cell_b;

    this->new_output.th_idx = st0_th_idx;
    this->new_output.th_valid = st0_th_valid;
    this->new_output.cell_a = st0_cell_a;
    this->new_output.cell_b = st0_cell_b;
    this->new_output.node_a = c2n[idxa];
    this->new_output.node_b = c2n[idxb];
    this->new_output.sw.th_idx = st9_sw.th_idx;
    this->new_output.sw.th_valid = st9_sw.th_valid;
    this->new_output.sw.sw = st9_sw.sw;
    this->new_output.wa.th_idx = wa.th_idx;
    this->new_output.wa.cell = wa.cell;
    this->new_output.wa.node = wa.node;
    this->new_output.wb.th_idx = wb.th_idx;
    this->new_output.wb.cell = wb.cell;
    this->new_output.wb.node = wb.node;
}