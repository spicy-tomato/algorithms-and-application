#include <iterator>

#ifndef RED_BLACK_TREE_ITERATOR
#define RED_BLACK_TREE_ITERATOR

template<class Key, class Value>
class RedBlackTreeIterator : public std::iterator<std::bidirectional_iterator_tag, RedBlackTreeNode<Key, Value>> {
    private:
        typedef RedBlackTreeNode<Key, Value> Node;

        void update();

    protected:
        Node *iterator;

    public:
        Key   first;
        Value second;

        explicit RedBlackTreeIterator(Node* iterator = nullptr);

        Node& operator*();

        RedBlackTreeIterator operator++();

        RedBlackTreeIterator operator++(int);

        RedBlackTreeIterator operator--();

        RedBlackTreeIterator operator--(int);

        bool operator==(const RedBlackTreeIterator<Key, Value>& that);

        bool operator!=(const RedBlackTreeIterator<Key, Value>& that);
};

template<class Key, class Value>
void RedBlackTreeIterator<Key, Value>::update() {
    if (iterator != nullptr) {
        first  = iterator->key;
        second = iterator->value;
    }
    else {
        first  = NULL;
        second = NULL;
    }
}

template<class Key, class Value>
RedBlackTreeIterator<Key, Value>::RedBlackTreeIterator(Node* iterator) {
    this->iterator = iterator;
    if (iterator != nullptr) {
        update();
    }
}

template<class Key, class Value>
typename RedBlackTreeIterator<Key, Value>::Node& RedBlackTreeIterator<Key, Value>::operator*() {
    return iterator;
}

template<class Key, class Value>
RedBlackTreeIterator<Key, Value> RedBlackTreeIterator<Key, Value>::operator++() {
    iterator = iterator->successor();
    update();
    return *this;
}

template<class Key, class Value>
RedBlackTreeIterator<Key, Value> RedBlackTreeIterator<Key, Value>::operator++(int) {
    RedBlackTreeIterator temp = *this;
    ++*this;
    return temp;
}

template<class Key, class Value>
RedBlackTreeIterator<Key, Value> RedBlackTreeIterator<Key, Value>::operator--() {
    iterator = iterator->predecessor();
    update();
    return *this;
}

template<class Key, class Value>
RedBlackTreeIterator<Key, Value> RedBlackTreeIterator<Key, Value>::operator--(int) {
    Node* temp = iterator;
    operator--();
    return RedBlackTreeIterator<Key, Value>(temp);
}

template<class Key, class Value>
bool RedBlackTreeIterator<Key, Value>::operator==(const RedBlackTreeIterator<Key, Value>& that) {
    return iterator == that.iterator;
}

template<class Key, class Value>
bool RedBlackTreeIterator<Key, Value>::operator!=(const RedBlackTreeIterator<Key, Value>& that) {
    return iterator != that.iterator;
}

#endif //RED_BLACK_TREE_ITERATOR
