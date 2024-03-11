
#ifndef CPP_PIPELINE_SA_HLS_H
#define CPP_PIPELINE_SA_HLS_H

#include "defines_sa_hls.hpp"

#include "stage0_sa_hls.hpp"
#include "stage1_sa_hls.hpp"
#include "stage2_sa_hls.hpp"
#include "stage3_sa_hls.hpp"
#include "stage4_sa_hls.hpp"
#include "stage5_sa_hls.hpp"
#include "stage6_sa_hls.hpp"
#include "stage7_sa_hls.hpp"
#include "stage8_sa_hls.hpp"
#include "stage9_sa_hls.hpp"

class PipelineSaHls
{
private:
public:
    void run_single(int (&n2c)[N_COPIES][N_THREADS][N_CELLS], int (&c2n)[N_COPIES][N_THREADS][N_CELLS],
                    int (&n)[N_CELLS][N_NEIGH]);

private:
    static void exec_pipeline(int (&n2c)[N_THREADS][N_CELLS], int (&c2n)[N_THREADS][N_CELLS], int (&n)[N_CELLS][N_NEIGH]);
};

#endif
