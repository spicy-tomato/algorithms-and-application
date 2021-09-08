#ifndef RED_BLACK_TREE_H
#define RED_BLACK_TREE_H

template<class Key, class Value>
class RedBlackTree<Key, Value> {
    private:
        // Static constants
        static const bool RED = true;
        static const bool BLACK = false;

        // Inner class
        class Node {
            public:
                // Node's props
                Key key;
                Value value;
                Node left, right;
                int N = 0;
                bool color = RED;

                // Node's constructor
                Node(Key key, Value value, int N, bool color);
        };

        // Props
        Node root;

        // Private methods
        Node rotateLeft(Node h);
        Node rotateRight(Node h);
        void flipColors(Node h);
        int size(Node h);
        bool isRed(Node h);
        Node put(Node h, Key key, Value value);

    public:
        // Constructor
        RedBlackTree();

        // Methods
        int size();
        void put(Key key, Value value);
};

#endif //RED_BLACK_TREE_H
