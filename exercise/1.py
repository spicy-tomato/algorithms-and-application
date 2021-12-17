from queue import PriorityQueue


class HuffmanNodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self) -> tuple:
        return self.left, self.right

    def nodes(self) -> tuple:
        return self.left, self.right

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffman_code_tree(node, bin_string='') -> dict:
    if type(node) is str:
        return {node: bin_string}
    (l, r) = node.children()
    d = {}
    d.update(huffman_code_tree(l, bin_string + '0'))
    d.update(huffman_code_tree(r, bin_string + '1'))
    return d


def run():
    data = ['a', 'b', 'c', 'd', 'e', 'f']
    freq = [5, 9, 12, 13, 16, 45]
    list_freq = []
    for i in range(len(data)):
        list_freq.append((data[i], freq[i]))

    list_freq.sort(reverse=True)

    pq = PriorityQueue()
    pq.put((12, 'c'))
    pq.put((45, 'f'))
    pq.put((5, 'a'))
    pq.put((9, 'b'))
    pq.put((13, 'd'))
    pq.put((16, 'e'))

    while pq.qsize() > 1:
        (key1, c1) = pq.get()
        (key2, c2) = pq.get()
        node = HuffmanNodeTree(c1, c2)
        pq.put((key1 + key2, node))

    huffman_code = huffman_code_tree(pq.get()[1])

    print('Char => Huffman code ')
    for i in range(len(list_freq)):
        print('{} => {:<}'.format(list_freq[i][0], huffman_code[list_freq[i][0]]))


run()
