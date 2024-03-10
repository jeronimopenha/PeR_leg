#include "sa_pipeline_sw.h"
#include "stage0_sa.cpp"
#include "stage1_sa.cpp"
#include "stage2_sa.cpp"
#include "stage3_sa.cpp"
#include "stage4_sa.cpp"
#include "stage5_sa.cpp"
#include "stage6_sa.cpp"
#include "stage7_sa.cpp"
#include "stage8_sa.cpp"
#include "stage9_sa.cpp"


class SAPipelineSw {
private:
public:
    void run_single(int (&n2c)[N_COPIES][N_THREADS][N_CELLS], int (&c2n)[N_COPIES][N_THREADS][N_CELLS],
                    int (&n)[N_CELLS][N_NEIGH]) {

        for (int i = 0; i < N_COPIES; ++i) {
            exec_pipeline(n2c[i], c2n[i], n);
        }
    }

private:
    static void
    exec_pipeline(int (&n2c)[N_THREADS][N_CELLS], int (&c2n)[N_THREADS][N_CELLS], int (&n)[N_CELLS][N_NEIGH]) {

        Stage0SA st0 = Stage0SA();
        Stage1SA st1 = Stage1SA();
        Stage2SA st2 = Stage2SA();
        Stage3SA st3 = Stage3SA();
        Stage4SA st4 = Stage4SA();
        Stage5SA st5 = Stage5SA();
        Stage6SA st6 = Stage6SA();
        Stage7SA st7 = Stage7SA();
        Stage8SA st8 = Stage8SA();
        Stage9SA st9 = Stage9SA();


        for (long counter = 0; counter < MAX_COUNTER; counter++) {
            st0.compute();
            st1.compute(st0.old_output, st9.old_output, st1.old_output.wb, c2n);
            st2.compute(st1.old_output, n);
            st3.compute(st2.old_output, st3.old_output.wb, n2c);
            st4.compute(st3.old_output);
            st5.compute(st4.old_output);
            st6.compute(st5.old_output);
            st7.compute(st6.old_output);
            st8.compute(st7.old_output);
            st9.compute(st8.old_output);
        }
    }
};