#include <iostream>
#include "red_black_tree/red_black_tree.cpp"
#include <map>

int main() {
    RedBlackTree<int, int> tree;

    for (int i = 0; i < 5; ++i) {
        tree.insert(i, i*i);
    }

    std::cout << tree.get(2) << '\n';
    std::cout << tree.size() << '\n';
    tree.erase(3);
    std::cout << tree.size() << '\n';

    std::map<int, int> m;

    return 0;
}
