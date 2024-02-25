#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <unordered_map>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#include "stage0_sa.cpp"
#include "src/sw/sa_pipeline/stage10_sa.hpp"
#include "src/sw/sa_pipeline/stage1_sa.hpp"
#include "src/sw/sa_pipeline/stage2_sa.hpp"
#include "src/sw/sa_pipeline/stage3_sa.hpp"
#include "src/sw/sa_pipeline/stage4_sa.hpp"
#include "src/sw/sa_pipeline/stage5_sa.hpp"
#include "src/sw/sa_pipeline/stage6_sa.hpp"
#include "src/sw/sa_pipeline/stage7_sa.hpp"
#include "src/sw/sa_pipeline/stage8_sa.hpp"
#include "src/sw/sa_pipeline/stage9_sa.hpp"
#include "src/util/per_enum.hpp"
#include "src/python/util/per_graph.hpp"
#include "src/python/util/piplinebase.hpp"
#include "src/util/util.hpp"

class SAPipeline : public PiplineBase {
private:
    int len_pipeline;
public:
    SAPipeline(PeRGraph per_graph, ArchType arch_type, int distance_table_bits, bool make_shuffle, int n_threads)
        : len_pipeline(10), PiplineBase(per_graph, arch_type, distance_table_bits, make_shuffle, len_pipeline, n_threads) {}

    std::unordered_map<int, std::vector<int>> run_parallel(int n_copies = 1) {
        int max_jobs = sysconf(_SC_NPROCESSORS_ONLN);
        int exec_times = 1000;
        int max_counter = pow(per_graph.n_cells, 2) * exec_times;
        std::unordered_map<int, std::vector<int>> dic_man;
        std::unordered_map<std::string, std::vector<int>> reports;
        std::vector<pid_t> jobs_alive;
        
        for (int exec_num = 0; exec_num < n_copies; ++exec_num) {
            pid_t pid = fork();
            if (pid == 0) {
                exec_pipeline(exec_num, max_counter, dic_man);
                exit(0);
            } else if (pid > 0) {
                jobs_alive.push_back(pid);
            } else {
                std::cerr << "Error in forking process" << std::endl;
                exit(1);
            }

            while (jobs_alive.size() >= max_jobs) {
                std::vector<pid_t> alive;
                for (auto job : jobs_alive) {
                    if (waitpid(job, NULL, WNOHANG) == 0) {
                        alive.push_back(job);
                    }
                }
                jobs_alive = alive;
                sleep(1);
            }
        }

        while (!jobs_alive.empty()) {
            std::vector<pid_t> alive;
            for (auto job : jobs_alive) {
                if (waitpid(job, NULL, WNOHANG) == 0) {
                    alive.push_back(job);
                }
            }
            jobs_alive = alive;
            sleep(1);
        }

        for (auto &[k, v] : dic_man) {
            int exec_num = v[0];
            int exec_counter = v[1];
            std::vector<int> n2c = v[2];
            std::string exec_key = "exec_" + std::to_string(exec_num);
            reports[exec_key] = Util::create_exec_report(this, exec_num, max_counter, std::vector<int>(n_threads, exec_counter), n2c);
        }

        return Util::create_report(this, "SA_PIPELINE", n_copies, reports);
    }

    std::unordered_map<int, std::vector<int>> run_single(int n_copies = 1) {
        int exec_times = 1000;
        int max_counter = pow(per_graph.n_cells, 2) * exec_times;
        std::unordered_map<int, std::vector<int>> dic_man;
        std::unordered_map<std::string, std::vector<int>> reports;

        for (int exec_num = 0; exec_num < n_copies; ++exec_num) {
            exec_pipeline(exec_num, max_counter, dic_man);
        }

        for (auto &[k, v] : dic_man) {
            int exec_num = v[0];
            int exec_counter = v[1];
            std::vector<int> n2c = v[2];
            std::string exec_key = "exec_" + std::to_string(exec_num);
            reports[exec_key] = Util::create_exec_report(this, exec_num, max_counter, std::vector<int>(n_threads, exec_counter), n2c);
        }

        return Util::create_report(this, "SA_PIPELINE", n_copies, reports);
    }

private:
    void exec_pipeline(int exec_key, int max_counter, std::unordered_map<int, std::vector<int>> &dic_man) {
        std::unordered_map<int, std::vector<int>> n2c;
        std::unordered_map<int, std::vector<int>> c2n;
        
        std::shared_ptr<Stage0SA> st0 = std::make_shared<Stage0SA>(per_graph.n_cells, n_threads);
        std::shared_ptr<Stage1SA> st1 = std::make_shared<Stage1SA>(c2n, n_threads);
        std::shared_ptr<Stage2SA> st2 = std::make_shared<Stage2SA>(per_graph.neighbors);
        std::shared_ptr<Stage3SA> st3 = std::make_shared<Stage3SA>(n2c, n_threads);
        std::shared_ptr<Stage4SA> st4 = std::make_shared<Stage4SA>(arch_type, n_lines, n_columns);
        std::shared_ptr<Stage5SA> st5 = std::make_shared<Stage5SA>(arch_type, n_lines, n_columns);
        std::shared_ptr<Stage6SA> st6 = std::make_shared<Stage6SA>();
        std::shared_ptr<Stage7SA> st7 = std::make_shared<Stage7SA>();
        std::shared_ptr<Stage8SA> st8 = std::make_shared<Stage8SA>();
        std::shared_ptr<Stage9SA> st9 = std::make_shared<Stage9SA>();
        std::shared_ptr<Stage10SA> st10 = std::make_shared<Stage10SA>();
        
        int counter = 0;
        while (counter < max_counter) {
            st0->compute();
            st1->compute(st0->get_old_output(), st9->get_old_output(), st1->get_old_output()["wb"]);
            st2->compute(st1->get_old_output());
            st3->compute(st2->get_old_output(), st3->get_old_output()["wb"]);
            st4->compute(st3->get_old_output());
            st5->compute(st4->get_old_output());
            st6->compute(st5->get_old_output());
            st7->compute(st6->get_old_output());
            st8->compute(st7->get_old_output());
            st9->compute(st8->get_old_output());
            st10->compute(st9->get_old_output());

            counter++;
        }

        for (int th_idx = 0; th_idx < n_threads; ++th_idx) {
            for (int n_idx = 0; n_idx < n2c[th_idx].size(); ++n_idx) {
                if (n2c[th_idx][n_idx] != -1) {
                    n2c[th_idx][n_idx] = Util::get_line_column_from_cell(n2c[th_idx][n_idx], n_lines, n_columns);
                } else {
                    n2c[th_idx][n_idx] = {-1, -1};
                }
            }
        }

        dic_man[getpid()] = {exec_key, st0->get_exec_counter(), n2c};
    }
};