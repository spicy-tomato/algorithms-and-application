#include "../red_black_tree/red_black_tree.cpp"

#ifndef MAP
#define MAP

template<class Key, class Value>
class Map {
    private:
        // Props
        RedBlackTree<Key, Value> tree;

    public:
        typedef typename RedBlackTree<Key, Value>::iterator iterator;

        iterator max();

        iterator min();

        iterator begin();

        iterator end();

        bool empty();

        int size();

        void insert(Key key, Value value);

        void erase(Key key);

        void clear();

        Value& operator[](Key key);
};

template<class Key, class Value>
typename Map<Key, Value>::iterator Map<Key, Value>::max() {
    return tree.max();
}

template<class Key, class Value>
typename Map<Key, Value>::iterator Map<Key, Value>::min() {
    return tree.min();
}

template<class Key, class Value>
typename Map<Key, Value>::iterator Map<Key, Value>::begin() {
    return tree.begin();
}

template<class Key, class Value>
typename Map<Key, Value>::iterator Map<Key, Value>::end() {
    return tree.end();
}

template<class Key, class Value>
bool Map<Key, Value>::empty() {
    return tree.empty();
}

template<class Key, class Value>
int Map<Key, Value>::size() {
    return tree.size();
}

template<class Key, class Value>
void Map<Key, Value>::insert(Key key, Value value) {
    tree.insert(key, value);
}

template<class Key, class Value>
void Map<Key, Value>::erase(Key key) {
    tree.erase(key);
}

template<class Key, class Value>
void Map<Key, Value>::clear() {
    tree.clear();
}

template<class Key, class Value>
Value& Map<Key, Value>::operator[](Key key) {
    try {
        return tree.find(key);
    }
    catch (invalid_key<Key>& ex) {
        Value value;
        tree.insert(key, value);
        return tree.find(key);
    }
}

#endif //MAP
