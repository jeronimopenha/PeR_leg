#include "pipeline_sa_hls.hpp"

void PipelineSaHls::run_single(ap_int<8> *n2c0, ap_int<8> *n2c1, ap_int<8> *n2c2, ap_int<8> *n2c3, ap_int<8> *c2n, ap_int<8> *n0, ap_int<8> *n1, ap_int<8> *n2, ap_int<8> *n3)
{

    for (ap_int<8> i = 0; i < N_COPIES; ++i)
    {
        exec_pipeline(n2c0, n2c1, n2c2, n2c3, c2n, n0, n1, n2, n3, i);
    }
}

void PipelineSaHls::exec_pipeline(ap_int<8> *n2c0, ap_int<8> *n2c1, ap_int<8> *n2c2, ap_int<8> *n2c3, ap_int<8> *c2n, ap_int<8> *n0, ap_int<8> *n1, ap_int<8> *n2, ap_int<8> *n3, ap_int<8> exec_n)
{

    Stage0SaHls st0;
    Stage1SaHls st1;
    Stage2SaHls st2;
    Stage3SaHls st3;
    Stage4SaHls st4;
    Stage5SaHls st5;
    Stage6SaHls st6;
    Stage7SaHls st7;
    Stage8SaHls st8;
    Stage9SaHls st9;

    ap_int<8> exec_offset = exec_n * N_THREADS * N_CELLS;

    for (long counter = 0; counter < MAX_COUNTER; counter++)
    {
#pragma HLS pipeline
        st0.compute();
        st1.compute(st0.m_old_output, st9.m_old_output, st1.m_old_output.wb, c2n, exec_offset);
        st2.compute(st1.m_old_output, n0, n1, n2, n3);
        st3.compute(st2.m_old_output, st3.m_old_output.wb, n2c0, n2c1, n2c2, n2c3, exec_offset);
        st4.compute(st3.m_old_output);
        st5.compute(st4.m_old_output);
        st6.compute(st5.m_old_output);
        st7.compute(st6.m_old_output);
        st8.compute(st7.m_old_output);
        st9.compute(st8.m_old_output);
    }
}
