#include<vector>

#ifndef HEAP
#define HEAP

template<class Key>
class Heap {
    private:
        // Props
        std::vector<Key> queue = {NULL};

        // Private methods
        void swap(int i, int j);

        void swim(int k);

        void sink(int k);

    public:
        // Constructor
        Heap();

        // Public methods
        int empty();

        int size();

        void insert(Key v);

        Key remove();

        Key max();
};

template<class Key>
void Heap<Key>::swap(int i, int j) {
    Key temp = queue[i];
    queue[i] = queue[j];
    queue[j] = temp;
}

template<class Key>
void Heap<Key>::swim(int k) {
    while (k > 1 && queue[k / 2] < queue[k]) {
        swap(k / 2, k);
        k = k / 2;
    }
}

template<class Key>
void Heap<Key>::sink(int k) {
    while (2 * k <= size()) {
        int j = 2 * k;
        if (j < size() && queue[j] < queue[j + 1]) {
            j++;
        }

        if (queue[k] >= queue[j]) {
            break;
        }

        swap(k, j);
        k = j;
    }
}

template<class Key>
Heap<Key>::Heap() = default;

template<class Key>
int Heap<Key>::empty() {
    return queue.size() <= 1;
}

template<class Key>
int Heap<Key>::size() {
    return queue.size() - 1;
}

template<class Key>
void Heap<Key>::insert(Key v) {
    queue.push_back(v);
    swim(size());
}

template<class Key>
Key Heap<Key>::remove() {
    Key max = queue[1];
    swap(1, queue.size() - 1);
    queue.pop_back();
    sink(1);

    return max;
}

template<class Key>
Key Heap<Key>::max() {
    return empty() ? NULL : queue[1];
}

#endif //HEAP