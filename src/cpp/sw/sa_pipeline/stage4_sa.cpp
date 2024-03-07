#include "sa_pipeline_sw.h"


class Stage4SA {
private:

public:
    ST4_OUT new_output = {
            0, false, 0, 0,
            {-1, -1, -1, -1},
            {-1, -1, -1, -1},
            {0, 0, 0, 0},
            {0, 0, 0, 0}
    };
    ST4_OUT old_output = {
            0, false, 0, 0,
            {-1, -1, -1, -1},
            {-1, -1, -1, -1},
            {0, 0, 0, 0},
            {0, 0, 0, 0}
    };

    void compute(ST3_OUT st3_input) {
        this->old_output = this->new_output;
        this->old_output = this->new_output;
        this->old_output = this->new_output;
        this->old_output = this->new_output;
        memcpy(&this->old_output.cva, &this->new_output.cva, sizeof(this->new_output.cva));
        memcpy(&this->old_output.cvb, &this->new_output.cvb, sizeof(this->new_output.cvb));
        memcpy(&this->old_output.dvac, &this->new_output.dvac, sizeof(this->new_output.dvac));
        memcpy(&this->old_output.dvbc, &this->new_output.dvbc, sizeof(this->new_output.dvbc));

        int st3_th_idx = st3_input.th_idx;
        bool st3_th_valid = st3_input.th_valid;
        int st3_cell_a = st3_input.cell_a;
        int st3_cell_b = st3_input.cell_b;


        if (st3_th_idx == 0 && st3_th_valid) {
            int a = 1;
        }

        int dvac[4] = {0, 0, 0, 0};
        int dvbc[4] = {0, 0, 0, 0};

        int ca = st3_cell_a;
        int cb = st3_cell_b;

        for (int n = 0; n < N_NEIGH; ++n) {

            int i1, i2, j1, j2;

            if (st3_input.cva[n] != -1) {
                get_line_column_from_cell(ca, N_LINES, N_COLUMNS, i1, j1);
                get_line_column_from_cell(st3_input.cva[n], N_LINES, N_COLUMNS, i2, j2);
#if defined(ONE_HOP)
                dvac[n] = dist_one_hop(i1, j1, i2, j2);
#elif defined(MESH)
                dvac[n] = dist_manhattan(i1, j1, i2, j2);
#endif
            }

            if (st3_input.cvb[n] != -1) {
                get_line_column_from_cell(cb, N_LINES, N_COLUMNS, i1, j1);
                get_line_column_from_cell(st3_input.cvb[n], N_LINES, N_COLUMNS, i2, j2);
#if defined(ONE_HOP)
                dvbc[n] = dist_one_hop(i1, j1, i2, j2);
#elif defined(MESH)
                dvbc[n] = dist_manhattan(i1, j1, i2, j2);
#endif
            }
        }

        this->new_output.th_idx = st3_th_idx;
        this->new_output.th_valid = st3_th_valid;
        this->new_output.cell_a = st3_cell_a;
        this->new_output.cell_b = st3_cell_b;
        memcpy(&this->new_output.cva, &st3_input.cva, sizeof(st3_input.cva));
        memcpy(&this->new_output.cvb, &st3_input.cvb, sizeof(st3_input.cvb));
        memcpy(&this->new_output.dvac, &dvac, sizeof(dvac));
        memcpy(&this->new_output.dvbc, &dvbc, sizeof(dvbc));
    }
};