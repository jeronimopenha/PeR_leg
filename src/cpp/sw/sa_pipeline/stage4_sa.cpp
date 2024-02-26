#include <iostream>

enum ArchType { ONE_HOP, MESH };

class Stage4SA {
private:
    ArchType arch_type;
    int n_lines;
    int n_columns;
    int* new_output;
    int* old_output;

public:
    Stage4SA(ArchType arch_type, int n_lines, int n_columns) :
        arch_type(arch_type),
        n_lines(n_lines),
        n_columns(n_columns)
    {
        new_output = new int[12]();
        old_output = new int[12]();
    }

    ~Stage4SA() {
        delete[] new_output;
        delete[] old_output;
    }

    void compute(int* st3_input) {
        std::copy(new_output, new_output + 12, old_output);

        int st3_th_idx = st3_input[0];
        bool st3_th_valid = st3_input[1];
        int st3_cell_a = st3_input[2];
        int st3_cell_b = st3_input[3];
        int* st3_cva = st3_input + 4;
        int* st3_cvb = st3_input + 8;

        int dvac[4] = {0, 0, 0, 0};
        int dvbc[4] = {0, 0, 0, 0};

        for (int i = 0; i < 4; ++i) {
            int ca = st3_input[2];
            int cb = st3_input[3];
            int cva = st3_cva[i];
            int cvb = st3_cvb[i];

            if (cva != -1) {
                if (arch_type == ONE_HOP) {
                    // Compute distance using one-hop algorithm
                    // dvac[i] = ...
                } else if (arch_type == MESH) {
                    // Compute Manhattan distance
                    // dvac[i] = ...
                }
            }

            if (cvb != -1) {
                if (arch_type == ONE_HOP) {
                    // Compute distance using one-hop algorithm
                    // dvbc[i] = ...
                } else if (arch_type == MESH) {
                    // Compute Manhattan distance
                    // dvbc[i] = ...
                }
            }
        }

        std::copy(st3_input, st3_input + 12, new_output);
        std::copy(dvac, dvac + 4, new_output + 4);
        std::copy(dvbc, dvbc + 4, new_output + 8);
    }
};