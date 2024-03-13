#ifndef SA_TOP_H
#define SA_TOP_H

#include <cstring>
#include "ap_int.h"
#include "hls_stream.h"
#include "src/pipeline_sa_hls.hpp"

extern "C" void simulatedAnnealingTop(int *n2c,int *c2n,int *n);

#endif
