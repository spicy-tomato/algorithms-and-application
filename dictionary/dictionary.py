import string
from typing import Optional


class Node:
    def __init__(self, word: str, meaning: str = None):
        self.word = word
        self.children: dict[str, Optional[Node]] = self.__create_children()
        self.meaning = meaning

    @staticmethod
    def __create_children() -> dict[str, None]:
        children: dict[str, None] = {}
        for c in string.ascii_lowercase:
            children[c] = None
        for c in [' ', '.', '-', '\'']:
            children[c] = None
        return children


class Dictionary:
    def __init__(self):
        self.root: Node = Node('')

    def insert(self, word: str, meaning: str) -> None:
        curr: Node = self.root

        for i, char in enumerate(word):
            key = char.lower()
            if curr.children[key] is None:
                curr.children[key] = Node(word)
            if i == len(word) - 1:
                curr.children[key] = Node(word, meaning)
            curr = curr.children[key]

    def search(self, word) -> (Optional[str], Optional[str]):
        return self.__query(word)

    def __query(self, word: str) -> (Optional[str], Optional[str]):
        curr = self.root

        for i, char in enumerate(word):
            char = char.lower()
            if curr.children[char] is None or (curr.children[char].meaning is None and i == len(word) - 1):
                return None, None
            curr = curr.children[char]

        return curr.word, curr.meaning


dictionary = Dictionary()
dictionary.insert("the", "(mạo từ) cái, con, người...")
dictionary.insert("a", "(mạo từ) một; một (như kiểu); một (nào đó)")
dictionary.insert("there", "(phó từ) ở đó, tại đó, chỗ đó, chỗ ấy, đấy")
dictionary.insert("answer", "(danh từ) sự trả lời; câu trả lời; thư trả lời; lời đối đáp")
dictionary.insert("any", "(tính từ) một, một (người, vật) nào đó (trong câu hỏi)")
dictionary.insert("by", "(danh từ) gần, cạnh, kế, bên")
dictionary.insert("bye", "(thán từ) Chào tạm biệt")
dictionary.insert("their", "(tính từ sở hữu) của chúng, của chúng nó, của họ")

for wordSearch in ["the", "their", "thei"]:
    _word, _meaning = dictionary.search(wordSearch)
    print("{0} -> {1}: {2}".format(wordSearch, _word, _meaning))
