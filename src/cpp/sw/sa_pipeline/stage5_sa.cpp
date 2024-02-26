#include <iostream>

enum ArchType { ONE_HOP, MESH };

class Stage5SA {
private:
    ArchType arch_type;
    int n_lines;
    int n_columns;
    int* new_output;
    int* old_output;

public:
    Stage5SA(ArchType arch_type, int n_lines, int n_columns) :
        arch_type(arch_type),
        n_lines(n_lines),
        n_columns(n_columns)
    {
        new_output = new int[14]();
        old_output = new int[14]();
    }

    ~Stage5SA() {
        delete[] new_output;
        delete[] old_output;
    }

    void compute(int* st4_input) {
        std::copy(new_output, new_output + 14, old_output);

        int st4_th_idx = st4_input[0];
        bool st4_th_valid = st4_input[1];
        int st4_cbs = st4_input[2];
        int st4_cas = st4_input[3];
        int* st4_cva = st4_input + 4;
        int* st4_cvb = st4_input + 8;
        int* st4_dvac = st4_input + 12;
        int* st4_dvbc = st4_input + 14;

        int dvac[2] = {st4_dvac[0] + st4_dvac[1], st4_dvac[2] + st4_dvac[3]};
        int dvbc[2] = {st4_dvbc[0] + st4_dvbc[1], st4_dvbc[2] + st4_dvbc[3]};

        int dvas[4] = {0, 0, 0, 0};
        int dvbs[4] = {0, 0, 0, 0};

        for (int i = 0; i < 4; ++i) {
            if (st4_cva[i] != -1) {
                if (arch_type == ONE_HOP) {
                    dvas[i] = (st4_cas == st4_cva[i]) ?
                        // Compute distance using one-hop algorithm
                        // Util::dist_one_hop(...) :
                        0;
                } else if (arch_type == MESH) {
                    dvas[i] = (st4_cas == st4_cva[i]) ?
                        // Compute Manhattan distance
                        // Util::dist_manhattan(...) :
                        0;
                }
            }

            if (st4_cvb[i] != -1) {
                if (arch_type == ONE_HOP) {
                    dvbs[i] = (st4_cbs == st4_cvb[i]) ?
                        // Compute distance using one-hop algorithm
                        // Util::dist_one_hop(...) :
                        0;
                } else if (arch_type == MESH) {
                    dvbs[i] = (st4_cbs == st4_cvb[i]) ?
                        // Compute Manhattan distance
                        // Util::dist_manhattan(...) :
                        0;
                }
            }
        }

        std::copy(st4_input, st4_input + 14, new_output);
        std::copy(dvac, dvac + 2, new_output + 2);
        std::copy(dvbc, dvbc + 2, new_output + 4);
        std::copy(dvas, dvas + 4, new_output + 6);
        std::copy(dvbs, dvbs + 4, new_output + 10);
    }
};