#include "red_black_tree.h"

template<class Key, class Value>
RedBlackTree<Key, Value>::Node::Node(Key key, Value value, int N, bool color) {
    this->key   = key;
    this->value = value;
    this->N     = N;
    this->color = color;
}

template<class Key, class Value>
RedBlackTree<Key, Value>::RedBlackTree() = default;

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node RedBlackTree<Key, Value>::rotateLeft(RedBlackTree<Key, Value>::Node h) {
    Node x = h->right;

    h->right = x->left;
    x->left  = h;

    x->color = h->color;
    h->color = RED;

    x->N = h->N;
    h->N = size(x->left) + size(x->right) + 1;

    return x;
}

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node RedBlackTree<Key, Value>::rotateRight(RedBlackTree<Key, Value>::Node h) {
    Node x = h->left;

    h->left  = x->right;
    x->right = h;

    x->color = h->color;
    h->color = RED;

    x->N = h->N;
    h->N = size(x->right) + size(x->left) + 1;

    return x;
}

template<class Key, class Value>
void RedBlackTree<Key, Value>::flipColors(RedBlackTree<Key, Value>::Node h) {
    h->color = RED;
    h->left->color = h->right->color = BLACK;
}

template<class Key, class Value>
int RedBlackTree<Key, Value>::size(RedBlackTree<Key, Value>::Node h) {
    return h->N;
}

template<class Key, class Value>
bool RedBlackTree<Key, Value>::isRed(RedBlackTree<Key, Value>::Node h) {
    return h->color && h->color == RED;
}

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node RedBlackTree<Key, Value>::put(RedBlackTree<Key, Value>::Node h, Key key, Value value) {
    if (h == nullptr){
        return new Node(key, value, 1, RED);
    }

    if      (key < h.key) h.left  = put(h.left , key, value);
    else if (key > h.key) h.right = put(h.right, key, value);
    else h.value = value;

    if (isRed(h.right) && !isRed(h.left))      h = rotateLeft(h);
    if (isRed(h.left)  &&  isRed(h.left.left)) h = rotateRight(h);
    if (isRed(h.left)  &&  isRed(h.right))     flipColors(h);

    h.N = size(h.left) + size(h.right) + 1;
    return h;
}

template<class Key, class Value>
int RedBlackTree<Key, Value>::size() {
    return size(root);
}

template<class Key, class Value>
void RedBlackTree<Key, Value>::put(Key key, Value value) {
    root = put(root, key, value);
    root->color = BLACK;
}

