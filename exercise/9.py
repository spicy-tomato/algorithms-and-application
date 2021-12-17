ALPHABET_SIZE = 26
index = 0


class Node:
    def __init__(self):
        self.is_leaf = False
        self.children = [None] * ALPHABET_SIZE


def insert(word: str, root: Node) -> None:
    curr = root
    for char in word:
        idx = ord(char) - ord('a')
        if curr.children[idx] is None:
            curr.children[idx] = Node()
        curr = curr.children[idx]
    curr.isLeaf = True


def create_trie(words: [str], root: Node) -> None:
    for word in words:
        insert(word, root)


def count_children(node: Node) -> int:
    count = 0
    for i in range(ALPHABET_SIZE):
        if node.children[i] is not None:
            count += 1
            global index
            index = i
    return count


def traverse(root: Node) -> str:
    curr = root
    prefix = ""
    while count_children(curr) == 1 and curr.is_leaf is False:
        curr = curr.children[index]
        prefix += chr(ord('a') + index)
    return prefix or '-1'


def longest_common_prefix(arr: [str]) -> str:
    root = Node()
    create_trie(arr, root)
    return traverse(root)


def run() -> None:
    s = ['flower', 'flow', 'flight']
    print(longest_common_prefix(s))


run()
