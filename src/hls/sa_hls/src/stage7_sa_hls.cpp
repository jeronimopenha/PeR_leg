#include "stage7_sa_hls.hpp"

void Stage7SaHls::compute(ST6_OUT st6_input)
{
    m_old_output.th_idx = m_new_output.th_idx;
    m_old_output.th_valid = m_new_output.th_valid;
    m_old_output.dc = m_new_output.dc;
    m_old_output.dvas = m_new_output.dvas;
    m_old_output.dvbs = m_new_output.dvbs;

    int st6_th_idx = st6_input.th_idx;
    bool st6_th_valid = st6_input.th_valid;
    int st6_dvac = st6_input.dvac;
    int st6_dvbc = st6_input.dvbc;

    if (st6_th_idx == 0 && st6_th_valid)
    {
        int a = 1;
    }

    int dc = st6_dvac + st6_dvbc;
    int dvas = st6_input.dvas[0] + st6_input.dvas[1];
    int dvbs = st6_input.dvbs[0] + st6_input.dvbs[1];

    m_new_output.th_idx = st6_th_idx;
    m_new_output.th_valid = st6_th_valid;
    m_new_output.dc = dc;
    m_new_output.dvas = dvas;
    m_new_output.dvbs = dvbs;
}