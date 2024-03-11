//
// Created by jeronimo on 04/03/24.
//

#include "fifo_sa.h"

template<typename T>

class FifoSa {
private:
    T arr[CAPACITY];
    int capacity;
    int size;
    int front;
    int rear;

public:
    explicit FifoSa() {
        capacity = CAPACITY;
        //arr = new T[capacity];
        size = 0;
        front = 0;
        rear = -1;
    }

    ~FifoSa() {
        delete[] arr;
    }

    void enqueue(T data) {
        if (isFull()) {
            return;
        }
        rear = (rear + 1) % capacity;
        arr[rear] = data;
        size++;
    }

    T dequeue() {
        if (isEmpty()) {
            return {}; // Return default value for type T
        }
        T data = arr[front];
        front = (front + 1) % capacity;
        size--;
        return data;
    }

    T peek() {
        if (isEmpty()) {
            return {}; // Return default value for type T
        }
        return arr[front];
    }

    bool isEmpty() const {
        return size == 0;
    }

    bool isFull() const {
        return size == capacity;
    }

    int getSize() const {
        return size;
    }
};