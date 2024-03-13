#include "pipeline_sa_hls.hpp"

void PipelineSaHls::run_single(int *n2c, int *c2n, int *n)
{

    for (int i = 0; i < N_COPIES; ++i)
    {
        exec_pipeline(n2c, c2n, n, i);
    }
}

void PipelineSaHls::exec_pipeline(int *n2c, int *c2n, int *n, int exec_n)
{

    Stage0SaHls st0 = Stage0SaHls();
    Stage1SaHls st1 = Stage1SaHls();
    Stage2SaHls st2 = Stage2SaHls();
    Stage3SaHls st3 = Stage3SaHls();
    Stage4SaHls st4 = Stage4SaHls();
    Stage5SaHls st5 = Stage5SaHls();
    Stage6SaHls st6 = Stage6SaHls();
    Stage7SaHls st7 = Stage7SaHls();
    Stage8SaHls st8 = Stage8SaHls();
    Stage9SaHls st9 = Stage9SaHls();

    int exec_offset = exec_n * N_THREADS;

    for (long counter = 0; counter < MAX_COUNTER; counter++)
    {
        st0.compute();
        st1.compute(st0.old_output, st9.old_output, st1.old_output.wb, c2n, exec_offset);
        st2.compute(st1.old_output, n);
        st3.compute(st2.old_output, st3.old_output.wb, n2c, exec_offset);
        st4.compute(st3.old_output);
        st5.compute(st4.old_output);
        st6.compute(st5.old_output);
        st7.compute(st6.old_output);
        st8.compute(st7.old_output);
        st9.compute(st8.old_output);
    }
}
