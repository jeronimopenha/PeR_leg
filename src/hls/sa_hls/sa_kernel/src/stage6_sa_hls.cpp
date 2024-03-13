#include "stage6_sa_hls.hpp"

void Stage6SaHls::compute(ST5_OUT st5_input)
{
    m_old_output.th_idx = m_new_output.th_idx;
    m_old_output.th_valid = m_new_output.th_valid;
    m_old_output.dvac = m_new_output.dvac;
    m_old_output.dvbc = m_new_output.dvbc;
    m_old_output.dvas[0] = m_new_output.dvas[0];
    m_old_output.dvas[1] = m_new_output.dvas[1];
    m_old_output.dvbs[0] = m_new_output.dvbs[0];
    m_old_output.dvbs[1] = m_new_output.dvbs[1];

    int st5_th_idx = st5_input.th_idx;
    bool st5_th_valid = st5_input.th_valid;

    if (st5_th_idx == 0 && st5_th_valid)
    {
        int a = 1;
    }

    int dvac = st5_input.dvac[0] + st5_input.dvac[1];
    int dvbc = st5_input.dvbc[0] + st5_input.dvbc[1];
    int dvas[2] = {st5_input.dvas[0] + st5_input.dvas[1], st5_input.dvas[2] + st5_input.dvas[3]};
    int dvbs[2] = {st5_input.dvbs[0] + st5_input.dvbs[1], st5_input.dvbs[2] + st5_input.dvbs[3]};

    m_new_output.th_idx = st5_th_idx;
    m_new_output.th_valid = st5_th_valid;
    m_new_output.dvac = dvac;
    m_new_output.dvbc = dvbc;
    m_new_output.dvas[0] = dvas[0];
    m_new_output.dvas[1] = dvas[1];
    m_new_output.dvbs[0] = dvbs[0];
    m_new_output.dvbs[1] = dvbs[1];
}