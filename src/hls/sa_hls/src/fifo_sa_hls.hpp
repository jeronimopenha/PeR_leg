#ifndef CPP_FIFO_SA_HLS_H
#define CPP_FIFO_SA_HLS_H

#include "types_sa_hls.hpp"

#define CAPACITY 10

class FifoSaHls
{
private:
    W arr[CAPACITY];
    int capacity;
    int size;
    int front;
    int rear;

public:
    FifoSaHls();
    void enqueue(W data);
    W dequeue();
    W peek();
    bool isEmpty() const;
    bool isFull() const;
    int getSize() const;
};

#endif
