#include <iostream>

#ifndef RED_BLACK_TREE
#define RED_BLACK_TREE

template<class Key, class Value>
class RedBlackTree {
    private:
        // Static constants
        static const bool RED   = true;
        static const bool BLACK = false;

        // Inner class
        class Node {
            public:
                // Node's props
                Key   key;
                Value value;
                Node* left  = nullptr;
                Node* right = nullptr;
                int   N     = 0;
                bool  color = RED;

                // Node's constructor
                Node(Key key, Value value, int N, bool color);

                void assign(Node* node);
        };

        // Props
        Node* root = nullptr;

        // Private methods
        Node* rotateLeft(Node* head);

        Node* rotateRight(Node* head);

        void flipColors(Node* head);

        int size(Node* head);

        int updateSize(Node* head);

        bool isRed(Node* head);

        bool isBlack(Node* head);

        Node* insert(Node*& head, Key key, Value value);

        Node* erase(Node* head, Key key);

        void clear(Node* head);

        Node* balance(Node* head);

        Node* moveRedLeft(Node* head);

        Node* moveRedRight(Node* head);

        Node* eraseMin(Node* head);

        Node* eraseMax(Node* head);

        Node* min(Node* head);

    public:
        // Constructor
        RedBlackTree();

        // Destructor
        ~RedBlackTree();

        // Methods
        int size();

        int isEmpty();

        Value get(Key key);

        void insert(Key key, Value value);

        void erase(Key key);

        void eraseMin();

        void eraseMax();

        void clear();
};

template<class Key, class Value>
RedBlackTree<Key, Value>::Node::Node(Key key, Value value, int N, bool color) {
    this->key   = key;
    this->value = value;
    this->N     = N;
    this->color = color;
}

template<class Key, class Value>
void RedBlackTree<Key, Value>::Node::assign(Node* node) {
    key   = node->key;
    value = node->value;
}

template<class Key, class Value>
RedBlackTree<Key, Value>::RedBlackTree() = default;

template<class Key, class Value>
RedBlackTree<Key, Value>::~RedBlackTree() {
    clear();
}

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node* RedBlackTree<Key, Value>::rotateLeft(RedBlackTree<Key, Value>::Node* head) {
    if (head->right == nullptr) {
        return head;
    }

    Node* x = head->right;

    head->right = x->left;
    x->left     = head;

    x->color    = head->color;
    head->color = RED;

    x->N    = head->N;
    head->N = size(head->left) + size(head->right) + 1;

    return x;
}

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node* RedBlackTree<Key, Value>::rotateRight(RedBlackTree<Key, Value>::Node* head) {
    if (head->left == nullptr) {
        return head;
    }
    Node* x = head->left;

    head->left = x->right;
    x->right   = head;

    x->color    = head->color;
    head->color = RED;

    x->N    = head->N;
    updateSize(head);

    return x;
}

template<class Key, class Value>
void RedBlackTree<Key, Value>::flipColors(RedBlackTree<Key, Value>::Node* head) {
    head->color       = RED;
    head->left->color = head->right->color = BLACK;
}

template<class Key, class Value>
int RedBlackTree<Key, Value>::size(RedBlackTree<Key, Value>::Node* head) {
    return head != nullptr ? head->N : 0;
}

template<class Key, class Value>
int RedBlackTree<Key, Value>::updateSize(RedBlackTree::Node* head) {
    head->N = size(head->right) + size(head->left) + 1;
    return head->N;
}

template<class Key, class Value>
bool RedBlackTree<Key, Value>::isRed(RedBlackTree<Key, Value>::Node* head) {
    return head != nullptr && head->color == RED;
}

template<class Key, class Value>
bool RedBlackTree<Key, Value>::isBlack(RedBlackTree<Key, Value>::Node* head) {
    return !isRed(head);
}

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node* RedBlackTree<Key, Value>::insert(RedBlackTree<Key, Value>::Node*& head, Key key, Value value) {
    if (head == nullptr) {
        return new Node(key, value, 1, RED);
    }

    if      (key < head->key) head->left  = insert(head->left , key, value);
    else if (key > head->key) head->right = insert(head->right, key, value);
    else     head->value = value;

    if (isRed(head->right) && isBlack(head->left))     head = rotateLeft(head);
    if (isRed(head->left)  && isRed(head->left->left)) head = rotateRight(head);
    if (isRed(head->left)  && isRed(head->right))      flipColors(head);

    head->N = size(head->left) + size(head->right) + 1;
    return head;
}

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node* RedBlackTree<Key, Value>::erase(RedBlackTree<Key, Value>::Node* head, Key key) {
    if (key < head->key) {
        if (isBlack(head->left) && isBlack(head->left->left)) {
            head = moveRedLeft(head);
        }

        head->left = erase(head->left, key);
    }
    else {
        if (isRed(head->left)) {
            head = rotateRight(head);
        }

        if (head->key == key && head->right == nullptr) {
            return nullptr;
        }

        if (isBlack(head->right) && isBlack(head->right->left)) {
            head = moveRedRight(head);
        }

        if (head->key == key) {
            Node* x = min(head->right);
            head->assign(x);
            head->right = eraseMin(head->right);
        }
        else {
            head->right = erase(head->right, key);
        }
    }

    updateSize(head);

    return balance(head);
}

template<class Key, class Value>
void RedBlackTree<Key, Value>::clear(RedBlackTree<Key, Value>::Node* head) {
    if (head->left != nullptr) {
        clear(head->left);
    }

    if (head->right != nullptr) {
        clear(head->right);
    }

    delete head;
}

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node* RedBlackTree<Key, Value>::balance(Node* head) {
    if (isRed(head)) {
        head = rotateLeft(head);
    }

    return head;
}

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node* RedBlackTree<Key, Value>::moveRedLeft(RedBlackTree<Key, Value>::Node* head) {
    flipColors(head);

    if (isRed(head->right->left)) {
        head->right = rotateRight(head->right);
        head = rotateLeft(head);
    }

    return head;
}

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node* RedBlackTree<Key, Value>::moveRedRight(RedBlackTree<Key, Value>::Node* head) {
    flipColors(head);

    if (isRed(head->left->left)) {
        head = rotateRight(head->right);
    }

    return head;
}

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node* RedBlackTree<Key, Value>::eraseMin(RedBlackTree<Key, Value>::Node* head) {
    if (head->left == nullptr) {
        return nullptr;
    }

    if (isBlack(head->left) && isBlack(head->left->left)) {
        head = moveRedLeft(head);
    }

    head->left = eraseMin(head->left);

    return balance(head);
}

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node* RedBlackTree<Key, Value>::eraseMax(RedBlackTree<Key, Value>::Node* head) {
    if (isRed(head->left)) {
        head = rotateRight(head);
    }

    if (head->right == nullptr) {
        return nullptr;
    }

    if (isBlack(head->right) && isBlack(head->right->left)) {
        head = moveRedRight(head);
    }

    head->right = eraseMax(head->right);

    return balance(head);
}

template<class Key, class Value>
typename RedBlackTree<Key, Value>::Node* RedBlackTree<Key, Value>::min(RedBlackTree<Key, Value>::Node* head) {
    Node* minNode = head;
    while (minNode->left != nullptr) {
        minNode = minNode->left;
    }
    return minNode;
}

template<class Key, class Value>
int RedBlackTree<Key, Value>::size() {
    return size(root);
}

template<class Key, class Value>
int RedBlackTree<Key, Value>::isEmpty() {
    return size() == 0;
}

template<class Key, class Value>
Value RedBlackTree<Key, Value>::get(Key key) {
    Node* curr = root;
    while (curr != nullptr) {
        if (key == curr->key) {
            return curr->value;
        }

        if (key < curr->key) {
            curr = curr->left;
        }
        else {
            curr = curr->right;
        }
    }

    throw std::out_of_range("Cannot find");
}

template<class Key, class Value>
void RedBlackTree<Key, Value>::insert(Key key, Value value) {
    root = insert(root, key, value);
    root->color = BLACK;
}

template<class Key, class Value>
void RedBlackTree<Key, Value>::erase(Key key) {
    if (isBlack(root->left) && isBlack(root->right)) {
        root->color = RED;
    }

    root = erase(root, key);

    if (!isEmpty()) {
        root->color = BLACK;
    }
}

template<class Key, class Value>
void RedBlackTree<Key, Value>::eraseMin() {
    if (isBlack(root->left) && isBlack(root->right)) {
        root->color = RED;
    }

    root = eraseMin(root);

    if (!isEmpty()) {
        root->color = BLACK;
    }
}

template<class Key, class Value>
void RedBlackTree<Key, Value>::eraseMax() {
    if (isBlack(root->left) && isBlack(root->right)) {
        root->color = RED;
    }

    root = eraseMax(root);

    if (!isEmpty()) {
        root->color = BLACK;
    }
}

template<class Key, class Value>
void RedBlackTree<Key, Value>::clear() {
    clear(root);
}

#endif //RED_BLACK_TREE
