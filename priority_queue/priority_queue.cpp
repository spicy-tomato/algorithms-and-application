#include "../heap/heap.cpp"

#ifndef PRIORITY_QUEUE
#define PRIORITY_QUEUE

template<class Key>
class PriorityQueue {
    private:
        Heap<Key> heap;

    public:
        PriorityQueue();

        bool empty();

        Key top();

        void push(Key v);

        void pop();
};

template<class Key>
PriorityQueue<Key>::PriorityQueue() = default;

template<class Key>
bool PriorityQueue<Key>::empty() {
    return heap.empty();
}

template<class Key>
Key PriorityQueue<Key>::top() {
    return heap.max();
}

template<class Key>
void PriorityQueue<Key>::push(Key v) {
    heap.insert(v);
}

template<class Key>
void PriorityQueue<Key>::pop() {
    heap.remove();
}

#endif //PRIORITY_QUEUE
