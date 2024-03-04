//
// Created by jeronimo on 04/03/24.
//

#ifndef CPP_STAGE0_SA_H
#define CPP_STAGE0_SA_H

#include <cmath>

#include "defs_sa.h"

#define N_CELLS  100
#define N_CELLS_SQRT 10
#define N_CELLS_POW 10000
#define TH_BITS (int)ceil(log2(N_THREADS))
#define CELL_BITS (int)ceil(log2(N_CELLS))
#define MASK N_CELLS_POW-1

#endif //CPP_STAGE0_SA_H
