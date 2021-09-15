#ifndef RED_BLACK_TREE_NODE
#define RED_BLACK_TREE_NODE

template<class Key, class Value>
class RedBlackTreeNode {
    private:
        bool isLeftChild();

        bool isRightChild();

    public:
        // Static constants
        static const bool RED   = true;
        static const bool BLACK = false;

        // Node's props
        Key   key;
        Value value;
        RedBlackTreeNode* parent = nullptr;
        RedBlackTreeNode* left   = nullptr;
        RedBlackTreeNode* right  = nullptr;
        int               N      = 0;
        bool              color  = RED;

        // RedBlackTreeNode's constructor
        RedBlackTreeNode(Key key, Value value, int N, bool color, RedBlackTreeNode* parent = nullptr);

        void assign(RedBlackTreeNode* node);

        RedBlackTreeNode* min();

        RedBlackTreeNode* max();

        RedBlackTreeNode* predecessor();

        RedBlackTreeNode* successor();
};

template<class Key, class Value>
RedBlackTreeNode<Key, Value>::RedBlackTreeNode(Key key, Value value, int N, bool color, RedBlackTreeNode* parent) {
    this->parent = parent;
    this->key    = key;
    this->value  = value;
    this->N      = N;
    this->color  = color;
}

template<class Key, class Value>
bool RedBlackTreeNode<Key, Value>::isLeftChild() {
    return parent != nullptr && parent->left == this;
}

template<class Key, class Value>
bool RedBlackTreeNode<Key, Value>::isRightChild() {
    return parent != nullptr && parent->right == this;
}

template<class Key, class Value>
void RedBlackTreeNode<Key, Value>::assign(RedBlackTreeNode* node) {
    key   = node->key;
    value = node->value;
}

template<class Key, class Value>
RedBlackTreeNode<Key, Value>* RedBlackTreeNode<Key, Value>::min() {
    return left == nullptr ? this : left->min();
}

template<class Key, class Value>
RedBlackTreeNode<Key, Value>* RedBlackTreeNode<Key, Value>::max() {
    return right == nullptr ? this : right->max();
}

template<class Key, class Value>
RedBlackTreeNode<Key, Value>* RedBlackTreeNode<Key, Value>::predecessor() {
    if (this == nullptr) {
        return nullptr;
    }

    if (left != nullptr) {
        return left->max();
    }

    if (isRightChild()) {
        return parent;
    }

    RedBlackTreeNode<Key, Value>* curr = this;
    do {
        curr = curr->parent;
    }
    while (curr != nullptr && curr->isLeftChild());

    if (curr != nullptr) {
        return curr->parent;
    }
    return nullptr;
}

template<class Key, class Value>
RedBlackTreeNode<Key, Value>* RedBlackTreeNode<Key, Value>::successor() {
    if (this == nullptr) {
        return nullptr;
    }

    if (right != nullptr) {
        return right->min();
    }

    if (isLeftChild()) {
        return parent;
    }

    RedBlackTreeNode<Key, Value>* curr = this;
    do {
        curr = curr->parent;
    }
    while (curr != nullptr && curr->isRightChild());

    if (curr != nullptr) {
        return curr->parent;
    }
    return nullptr;
}

#endif //RED_BLACK_TREE_NODE
