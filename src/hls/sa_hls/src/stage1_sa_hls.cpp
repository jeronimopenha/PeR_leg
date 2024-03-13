#include "stage1_sa_hls.hpp"

Stage1SaHls::Stage1SaHls()
{
    m_flag = true;
    for (int i = 0; i < N_THREADS - 2; i++)
    {
        W fifo_cell_a = {0, 0, -1};
        W fifo_cell_b = {0, 0, -1};
        m_fifo_a.enqueue(fifo_cell_a);
        m_fifo_b.enqueue(fifo_cell_b);
    }
    for (int i = 0; i < N_THREADS; i++)
    {
        m_th_idx_offset[i] = i * N_CELLS;
    }
}

void Stage1SaHls::compute(ST0_OUT st0_input, ST9_OUT st9_sw, W st1_wb, int *c2n, int exec_offset)
{
    m_old_output.th_idx = m_new_output.th_idx;
    m_old_output.th_valid = m_new_output.th_valid;
    m_old_output.cell_a = m_new_output.cell_a;
    m_old_output.cell_b = m_new_output.cell_b;
    m_old_output.node_a = m_new_output.node_a;
    m_old_output.node_b = m_new_output.node_b;
    m_old_output.sw.th_idx = m_new_output.sw.th_idx;
    m_old_output.sw.th_valid = m_new_output.sw.th_valid;
    m_old_output.sw.sw = m_new_output.sw.sw;
    m_old_output.wa.th_idx = m_new_output.wa.th_idx;
    m_old_output.wa.cell = m_new_output.wa.cell;
    m_old_output.wa.node = m_new_output.wa.node;
    m_old_output.wb.th_idx = m_new_output.wb.th_idx;
    m_old_output.wb.cell = m_new_output.wb.cell;
    m_old_output.wb.node = m_new_output.wb.node;

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
        m_fifo_a.enqueue(W{m_new_output.th_idx, m_new_output.cell_a, m_new_output.node_b});
        m_fifo_b.enqueue(W{m_new_output.th_idx, m_new_output.cell_b, m_new_output.node_a});
    }

    W wa{};
    W wb{};
    if (st0_th_valid)
    {
        wa = m_fifo_a.dequeue();
        wb = m_fifo_b.dequeue();
    }
    else
    {
        wa.th_idx = m_new_output.wa.th_idx;
        wa.cell = m_new_output.wa.cell;
        wa.node = m_new_output.wa.node;
        wb.th_idx = m_new_output.wb.th_idx;
        wb.cell = m_new_output.wb.cell;
        wb.node = m_new_output.wb.node;
    }

    bool usw = m_new_output.sw.sw;
    W uwa{};
    W uwb{};
    uwa.th_idx = m_new_output.wa.th_idx;
    uwa.cell = m_new_output.wa.cell;
    uwa.node = m_new_output.wa.node;
    uwb.th_idx = st1_wb.th_idx;
    uwb.cell = st1_wb.cell;
    uwb.node = st1_wb.node;

    if (usw)
    {
        if (m_flag)
        {
            int idx = exec_offset + m_th_idx_offset[uwa.th_idx] + uwa.cell;
            c2n[idx] = wa.node;
            m_flag = !m_flag;
        }
        else
        {
            int idx = exec_offset + m_th_idx_offset[uwb.th_idx] + uwb.cell;
            c2n[idx] = uwb.node;
            m_flag = !m_flag;
        }
    }
    int idxa = exec_offset + m_th_idx_offset[st0_th_idx] + st0_cell_a;
    int idxb = exec_offset + m_th_idx_offset[st0_th_idx] + st0_cell_b;

    m_new_output.th_idx = st0_th_idx;
    m_new_output.th_valid = st0_th_valid;
    m_new_output.cell_a = st0_cell_a;
    m_new_output.cell_b = st0_cell_b;
    m_new_output.node_a = c2n[idxa];
    m_new_output.node_b = c2n[idxb];
    m_new_output.sw.th_idx = st9_sw.th_idx;
    m_new_output.sw.th_valid = st9_sw.th_valid;
    m_new_output.sw.sw = st9_sw.sw;
    m_new_output.wa.th_idx = wa.th_idx;
    m_new_output.wa.cell = wa.cell;
    m_new_output.wa.node = wa.node;
    m_new_output.wb.th_idx = wb.th_idx;
    m_new_output.wb.cell = wb.cell;
    m_new_output.wb.node = wb.node;
}