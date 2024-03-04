#include "defs_sa.h"

ST0_OUT st0_new_output, st0_old_output;
ST1_OUT st1_new_output, st1_old_output;
ST2_OUT st2_new_output, st2_old_output;
ST3_OUT st3_new_output, st3_old_output;
ST4_OUT st4_new_output, st4_old_output;
ST5_OUT st5_new_output, st5_old_output;
ST6_OUT st6_new_output, st6_old_output;
ST7_OUT st7_new_output, st7_old_output;
ST8_OUT st8_new_output, st8_old_output;
ST9_OUT st9_new_output, st9_old_output;


void init_outputs(){
    st0_new_output.th_idx = 0;
    st0_new_output.th_valid = 0;
    st0_new_output.cell_a = 0;
    st0_new_output.cell_b = 0;
    
}

void update_outputs(){

}

/*
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
};*/