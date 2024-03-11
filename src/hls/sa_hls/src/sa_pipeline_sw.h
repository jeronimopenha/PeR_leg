//
// Created by jeronimo on 04/03/24.
//

#ifndef CPP_SA_PIPELINE_SW_H
#define CPP_SA_PIPELINE_SW_H

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
                    int (&n)[N_CELLS][N_NEIGH]);

private:
    static void
    exec_pipeline(int (&n2c)[N_THREADS][N_CELLS], int (&c2n)[N_THREADS][N_CELLS], int (&n)[N_CELLS][N_NEIGH]);
};

#endif
