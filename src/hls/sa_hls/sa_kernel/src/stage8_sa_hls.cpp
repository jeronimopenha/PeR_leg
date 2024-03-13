#include "stage8_sa_hls.hpp"

void Stage8SaHls::compute(ST7_OUT st7_input)
{
    m_old_output.th_idx = m_new_output.th_idx;
    m_old_output.th_valid = m_new_output.th_valid;
    m_old_output.dc = m_new_output.dc;
    m_old_output.ds = m_new_output.ds;

    int st7_th_idx = st7_input.th_idx;
    bool st7_th_valid = st7_input.th_valid;
    int st7_dc = st7_input.dc;

    if (st7_th_idx == 0 && st7_th_valid)
    {
        int a = 1;
    }

    int st7_dvas = st7_input.dvas;
    int st7_dvbs = st7_input.dvbs;

    int ds = st7_dvas + st7_dvbs;

    m_new_output.th_idx = st7_th_idx;
    m_new_output.th_valid = st7_th_valid;
    m_new_output.dc = st7_dc;
    m_new_output.ds = ds;
}
