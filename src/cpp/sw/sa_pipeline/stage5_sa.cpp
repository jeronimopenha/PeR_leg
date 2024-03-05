#include <cstring>
#include "sa_pipeline_sw.h"

class Stage5SA {
private:
    ArchType arch_type;


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

    Stage5SA(ArchType arch_type) {
        this->arch_type = arch_type;
    }


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
        int *st4_cva = st4_input.cva;
        int *st4_cvb = st4_input.cvb;
        int *st4_dvac = st4_input.dvac;
        int *st4_dvbc = st4_input.dvbc;

        int dvac[2] = {st4_dvac[0] + st4_dvac[1], st4_dvac[2] + st4_dvac[3]};
        int dvbc[2] = {st4_dvbc[0] + st4_dvbc[1], st4_dvbc[2] + st4_dvbc[3]};

        int dvas[N_NEIGH] = {0, 0, 0, 0};
        int dvbs[N_NEIGH] = {0, 0, 0, 0};

        for (int n = 0; n < N_NEIGH; ++n) {
            if (st4_cva[n] != -1) {
                if (arch_type == ONE_HOP) {
                    dvas[n] = (st4_cas == st4_cva[n]) ?
                              // Compute distance using one-hop algorithm
                              // Util::dist_one_hop(...) :
                              0;
                } else if (arch_type == MESH) {
                    dvas[n] = (st4_cas == st4_cva[n]) ?
                              // Compute Manhattan distance
                              // Util::dist_manhattan(...) :
                              0;
                }
            }

            if (st4_cvb[n] != -1) {
                if (arch_type == ONE_HOP) {
                    dvbs[n] = (st4_cbs == st4_cvb[n]) ?
                              // Compute distance using one-hop algorithm
                              // Util::dist_one_hop(...) :
                              0;
                } else if (arch_type == MESH) {
                    dvbs[n] = (st4_cbs == st4_cvb[n]) ?
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