#include "sa_pipeline_sw.h"
#include "stage0_sa.cpp"
#include "stage1_sa.cpp"


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
        /*std::shared_ptr<Stage1SA> st1 = std::make_shared<Stage1SA>(c2n, n_threads);
        std::shared_ptr<Stage2SA> st2 = std::make_shared<Stage2SA>(per_graph.neighbors);
        std::shared_ptr<Stage3SA> st3 = std::make_shared<Stage3SA>(n2c, n_threads);
        std::shared_ptr<Stage4SA> st4 = std::make_shared<Stage4SA>(arch_type, n_lines, n_columns);
        std::shared_ptr<Stage5SA> st5 = std::make_shared<Stage5SA>(arch_type, n_lines, n_columns);
        std::shared_ptr<Stage6SA> st6 = std::make_shared<Stage6SA>();
        std::shared_ptr<Stage7SA> st7 = std::make_shared<Stage7SA>();
        std::shared_ptr<Stage8SA> st8 = std::make_shared<Stage8SA>();
        std::shared_ptr<Stage9SA> st9 = std::make_shared<Stage9SA>();
        std::shared_ptr<Stage10SA> st10 = std::make_shared<Stage10SA>();*/

        int counter = 0;
        while (counter < max_counter) {
            st0.compute();
            st1.compute(st0.old_output, SW(), W());
            /*st1->compute(st0->get_old_output(), st9->get_old_output(), st1->get_old_output()["wb"]);
            st2->compute(st1->get_old_output());
            st3->compute(st2->get_old_output(), st3->get_old_output()["wb"]);
            st4->compute(st3->get_old_output());
            st5->compute(st4->get_old_output());
            st6->compute(st5->get_old_output());
            st7->compute(st6->get_old_output());
            st8->compute(st7->get_old_output());
            st9->compute(st8->get_old_output());
            st10->compute(st9->get_old_output());*/

            counter++;
        }
    }
};