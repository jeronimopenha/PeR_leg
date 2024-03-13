#include "fifo_sa_hls.hpp"

FifoSaHls::FifoSaHls()
{
    m_capacity = CAPACITY;
    // arr = new T[capacity];
    m_size = 0;
    m_front = 0;
    m_rear = -1;
}

void FifoSaHls::enqueue(W data)
{
    if (isFull())
    {
        return;
    }
    m_rear = (m_rear + 1) % m_capacity;
    m_arr[m_rear] = data;
    m_size++;
}


W FifoSaHls::dequeue()
{
    if (isEmpty())
    {
        return {}; // Return default value for type T
    }
    W data = m_arr[m_front];
    m_front = (m_front + 1) % m_capacity;
    m_size--;
    return data;
}

W FifoSaHls::peek()
{
    if (isEmpty())
    {
        return {}; // Return default value for type T
    }
    return m_arr[m_front];
}

bool FifoSaHls::isEmpty() const
{
    return m_size == 0;
}

bool FifoSaHls::isFull() const
{
    return m_size == m_capacity;
}

int FifoSaHls::getSize() const
{
    return m_size;
}
