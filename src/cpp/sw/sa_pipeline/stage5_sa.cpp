#include "sa_pipeline_sw.h"


class Stage5SA {
private:

public:
    ST5_OUT new_output = {
            0, false,
            {0, 0},
            {0, 0},
            {0, 0, 0, 0},
            {0, 0, 0, 0}
    };
    ST5_OUT old_output = {
            0, false,
            {0, 0},
            {0, 0},
            {0, 0, 0, 0},
            {0, 0, 0, 0}
    };

    void compute(ST4_OUT st4_input) {
        this->old_output = this->new_output;
        this->old_output = this->new_output;
        memcpy(&this->old_output.dvac, &this->new_output.dvac, sizeof(this->new_output.dvac));
        memcpy(&this->old_output.dvbc, &this->new_output.dvbc, sizeof(this->new_output.dvbc));
        memcpy(&this->old_output.dvas, &this->new_output.dvas, sizeof(this->new_output.dvas));
        memcpy(&this->old_output.dvbs, &this->new_output.dvbs, sizeof(this->new_output.dvbs));

        int st4_th_idx = st4_input.th_idx;
        bool st4_th_valid = st4_input.th_valid;
        int st4_cbs = st4_input.cell_a;
        int st4_cas = st4_input.cell_b;


        if (st4_th_idx == 0 && st4_th_valid) {
            int a = 1;
        }

        int dvac[2] = {st4_input.dvac[0] + st4_input.dvac[1], st4_input.dvac[2] + st4_input.dvac[3]};
        int dvbc[2] = {st4_input.dvbc[0] + st4_input.dvbc[1], st4_input.dvbc[2] + st4_input.dvbc[3]};

        int dvas[N_NEIGH] = {0, 0, 0, 0};
        int dvbs[N_NEIGH] = {0, 0, 0, 0};

        for (int n = 0; n < N_NEIGH; ++n) {
            int i1, i2, j1, j2;

            if (st4_input.cva[n] != -1) {
                get_line_column_from_cell(st4_cas, N_LINES, N_COLUMNS, i1, j1);
                if (st4_cas == st4_input.cva[n]) {
                    get_line_column_from_cell(st4_cbs, N_LINES, N_COLUMNS, i2, j2);
                } else {
                    get_line_column_from_cell(st4_input.cva[n], N_LINES, N_COLUMNS, i2, j2);
                }
#if defined(ONE_HOP)
                dvas[n] = dist_one_hop(i1, j1, i2, j2);
#elif defined(MESH)
                dvas[n] = dist_manhattan(i1, j1, i2, j2);
#endif
            }

            if (st4_input.cvb[n] != -1) {
                get_line_column_from_cell(st4_cbs, N_LINES, N_COLUMNS, i1, j1);
                if (st4_cbs == st4_input.cvb[n]) {
                    get_line_column_from_cell(st4_cas, N_LINES, N_COLUMNS, i2, j2);
                } else {
                    get_line_column_from_cell(st4_input.cvb[n], N_LINES, N_COLUMNS, i2, j2);
                }
#if defined(ONE_HOP)
                dvbs[n] = dist_one_hop(i1, j1, i2, j2);
#elif defined(MESH)
                dvbs[n] = dist_manhattan(i1, j1, i2, j2);
#endif
            }
        }

        this->new_output.th_idx = st4_th_idx;
        this->new_output.th_valid = st4_th_valid;
        memcpy(&this->new_output.dvac, &dvac, sizeof(dvac));
        memcpy(&this->new_output.dvbc, &dvbc, sizeof(dvbc));
        memcpy(&this->new_output.dvas, &dvas, sizeof(dvas));
        memcpy(&this->new_output.dvbs, &dvbs, sizeof(dvbs));
    }
};