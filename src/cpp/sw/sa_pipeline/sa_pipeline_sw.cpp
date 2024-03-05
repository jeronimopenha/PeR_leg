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
    int len_pipeline;
public:
    static void run_single(int n_copies = 1) {
        int exec_times = 1000;
        int max_counter = N_CELLS_POW * exec_times;

        for (int exec_num = 0; exec_num < n_copies; ++exec_num) {
            exec_pipeline(exec_num, max_counter);
        }
    }

private:
    static void exec_pipeline(int exec_key, int max_counter) {
        int n2c[N_THREADS][N_CELLS];
        int c2n[N_THREADS][N_CELLS];

        Stage0SA st0 = Stage0SA();
        Stage1SA st1 = Stage1SA((int **) (c2n));
        Stage2SA st2 = Stage2SA();
        Stage3SA st3 = Stage3SA();
        Stage4SA st4 = Stage4SA();
        Stage5SA st5 = Stage5SA();
        Stage6SA st6 = Stage6SA();
        Stage7SA st7 = Stage7SA();
        Stage8SA st8 = Stage8SA();
        Stage9SA st9 = Stage9SA();


        int counter = 0;
        while (counter < max_counter) {
            st0.compute();
            st1.compute(st0.old_output, st9.old_output, st1.old_output.wb);
            st2.compute();
            st3.compute();
            st4.compute();
            st5.compute();
            st6.compute();
            st7.compute(st6.old_output);
            st8.compute(st7.old_output);
            st9.compute(st8.old_output);


            counter++;
        }
    }
};