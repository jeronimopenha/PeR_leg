#include <iostream>
#include <cmath>
#include "defs_sa.h"
#include "stage0_sa.h"

class Stage0SA {
private:
    int counter[N_THREADS] = {0, 0, 0, 0, 0, 0};
    int cell_a[N_THREADS] = {0, 0, 0, 0, 0, 0};
    int cell_b[N_THREADS] = {0, 0, 0, 0, 0, 0};
    bool th_valid[N_THREADS] = {false, false, false, false, false, false};
    int th_idx = 0;
    int exec_counter = 0;
    ST0_OUT new_output{0, 0, 0, 0};
    ST0_OUT old_output{0, 0, 0, 0};

public:

    void compute() {
        int th_idx_c = this->th_idx;

        this->old_output.th_idx = this->new_output.th_idx;
        this->old_output.th_valid = this->new_output.th_valid;
        this->old_output.cell_a = this->new_output.cell_a;
        this->old_output.cell_b = this->new_output.cell_b;


        if (!this->th_valid[th_idx_c]) {
            this->counter[th_idx_c] += 1;
            if (this->counter[th_idx_c] >= N_CELLS_POW) {
                this->counter[th_idx_c] = 0;
            }
            this->cell_a[th_idx_c] = this->counter[th_idx_c] & MASK;
            this->cell_b[th_idx_c] = (this->counter[th_idx_c] >> CELL_BITS) & MASK;

            this->th_idx += 1;
            if (this->th_idx == N_THREADS) {
                this->th_idx = 0;
            }
        }
        this->th_valid[th_idx_c] = !this->th_valid[th_idx_c];

        th_idx_c = this->th_idx;
        this->new_output.th_idx = this->th_idx;
        this->new_output.th_valid = this->th_valid[th_idx_c];
        this->new_output.cell_a = this->cell_a[th_idx_c];
        this->new_output.cell_b = this->cell_b[th_idx_c];

        if (this->th_valid[th_idx_c] && this->th_idx == 0) {
            this->exec_counter += 1;
        }
    }
};