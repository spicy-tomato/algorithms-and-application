from typing import Optional


class Student:
    def __init__(self, idx: str, name: str, is_male: bool, address: str, clazz: str, avg: float):
        self.idx = idx
        self.name = name
        self.is_male = is_male
        self.address = address
        self.clazz = clazz
        self.avg = avg


class Node:
    def __init__(self, student: Student = None):
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.value: Optional[Student] = student

    def insert(self, student: Student):
        if self.value is None:
            self.value = student
            return

        if student.idx < self.value.idx:
            if self.left is None:
                self.left = Node(student)
            else:
                self.left.insert(student)
            return

        if self.right is None:
            self.right = Node(student)
        else:
            self.right.insert(student)

    def search(self, idx: str) -> Optional[Student]:
        if self.value.idx == idx:
            return self.value

        if idx < self.value.idx:
            if self.left is None:
                return None
            return self.left.search(idx)

        if self.right is None:
            return None
        return self.right.search(idx)

    def remove(self, idx: str) -> bool:
        if idx < self.value.idx:
            if self.left is None:
                return False
            if self.left.value.idx == idx:
                if self.left.left is not None:
                    self.left = self.left.left
                elif self.left.right is not None:
                    self.left = self.left.right
                else:
                    self.left = None
                return True
            return self.left.remove(idx)

        if self.right is None:
            return False
        if self.right.value.idx == idx:
            if self.right.left is not None:
                self.right = self.right.left
            elif self.right.right is not None:
                self.right = self.right.right
            else:
                self.right = None
            return True
        return self.right.remove(idx)


class BinaryTree:
    def __init__(self):
        self.root = Node()

    def insert(self, student: Student):
        self.root.insert(student)

    def search(self, idx: str) -> Optional[Student]:
        return self.root.search(idx)

    def remove(self, idx: str) -> bool:
        if self.root is None:
            return False
        if self.root is None or self.root is None:
            self.root = None
            return True
        return self.root.remove(idx)


def run() -> None:
    s1 = Student('1', 'A', True, 'Hanoi', 'A1', 9.1)
    s2 = Student('2', 'C', True, 'HCM', 'C2', 8.2)
    s3 = Student('3', 'B', True, 'TQ', 'B3', 7.3)

    tree = BinaryTree()

    for student in [s1, s2, s3]:
        tree.insert(student)

    print(tree.search('2').name)

    print(tree.remove('0'))
    print(tree.remove('2'))

    print(tree.search('2'))


run()
