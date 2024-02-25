#include <iostream>
#include <cmath>

class Stage0SA
{
private:
    int *counter;
    int *cell_a;
    int *cell_b;
    bool *th_valid;
    int n_threads;
    int n_cells;
    int th_idx;
    int exec_counter;
    int th_bits;
    int cell_bits;
    int counter_mask;
    int *new_output;
    int *old_output;

public:
    Stage0SA(int n_cells, int n_threads) : n_threads(n_threads),
                                           n_cells(n_cells),
                                           th_idx(0),
                                           exec_counter(0)
    {
        th_bits = ceil(log2(n_threads));
        cell_bits = ceil(log2(n_cells));
        counter_mask = pow(ceil(sqrt(n_cells)), 2) - 1;

        counter = new int[n_threads]();
        cell_a = new int[n_threads]();
        cell_b = new int[n_threads]();
        th_valid = new bool[n_threads]();
        new_output = new int[4]();
        old_output = new int[4]();
    }

    ~Stage0SA()
    {
        delete[] counter;
        delete[] cell_a;
        delete[] cell_b;
        delete[] th_valid;
        delete[] new_output;
        delete[] old_output;
    }

    void compute()
    {
        int th_idx = this->th_idx;
        int cell_bits = this->cell_bits;
        int mask = this->counter_mask;

        this->old_output[0] = this->new_output[0];
        this->old_output[1] = this->new_output[1];
        this->old_output[2] = this->new_output[2];
        this->old_output[3] = this->new_output[3];

        if (!this->th_valid[th_idx])
        {
            this->counter[th_idx] += 1;
            if (this->counter[th_idx] >= pow(this->n_cells, 2))
            {
                this->counter[th_idx] = 0;
            }
            this->cell_a[th_idx] = this->counter[th_idx] & mask;
            this->cell_b[th_idx] = (this->counter[th_idx] >> cell_bits) & mask;

            this->th_idx += 1;
            if (this->th_idx == this->n_threads)
            {
                this->th_idx = 0;
            }
        }
        this->th_valid[th_idx] = !this->th_valid[th_idx];

        th_idx = this->th_idx;
        this->new_output[0] = this->th_idx;
        this->new_output[1] = this->th_valid[th_idx];
        this->new_output[2] = this->cell_a[th_idx];
        this->new_output[3] = this->cell_b[th_idx];
        if (this->th_valid[th_idx] && this->th_idx == 0)
        {
            this->exec_counter += 1;
        }
    }
};