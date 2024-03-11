#include "fifo_sa_hls.hpp"

FifoSaHls::FifoSaHls()
{
    capacity = CAPACITY;
    // arr = new T[capacity];
    size = 0;
    front = 0;
    rear = -1;
}

void FifoSaHls::enqueue(W data)
{
    if (isFull())
    {
        return;
    }
    rear = (rear + 1) % capacity;
    arr[rear] = data;
    size++;
}


W FifoSaHls::dequeue()
{
    if (isEmpty())
    {
        return {}; // Return default value for type T
    }
    W data = arr[front];
    front = (front + 1) % capacity;
    size--;
    return data;
}

W FifoSaHls::peek()
{
    if (isEmpty())
    {
        return {}; // Return default value for type T
    }
    return arr[front];
}

bool FifoSaHls::isEmpty() const
{
    return size == 0;
}

bool FifoSaHls::isFull() const
{
    return size == capacity;
}

int FifoSaHls::getSize() const
{
    return size;
}
