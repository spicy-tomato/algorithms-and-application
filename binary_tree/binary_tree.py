from node import Node


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            self.__insert(self.root, key, data)
        else:
            self.root = Node(key, data)

    def __insert(self, curr: Node, key, data):
        if key < curr.key:
            if curr.left:
                self.__insert(curr.left, key, data)
            else:
                curr.left = Node(key, data, curr)
        else:
            if curr.right:
                self.__insert(curr.right, key, data)
            else:
                curr.right = Node(key, data, curr)

    def find(self, key):
        if self.root:
            return self.__find(self.root, key)
        return None

    def __find(self, curr: Node, key):
        if key == curr.key:
            return curr.data

        if key < curr.key:
            if curr.left:
                return self.__find(curr.left, key)
            else:
                return None

        # key > curr.key
        if curr.right:
            return self.__find(curr.right, key)
        return None

    def delete(self, key):
        self.root = self.__delete(self.root, key)

        if self.root is None:
            return

        if key == self.root:
            if self.root.left:
                if self.root.left.right:
                    most_right = self.root.left.left.most_right()
                    most_right.right = self.root.left.right
                    self.root.left.right.parent = most_right
                self.root.left.parent = None
                self.root.left.right = self.root.right
                self.root.right.parent = self.root.left
                self.root = self.root.left
            elif self.root.right:
                self.root.right.parent = None
                self.root = self.root.right
            else:
                self.root = None

        self.__delete(self.root, key)

    def __delete(self, curr: Node, key):
        if curr is None:
            return None

        if key < curr.key:
            curr.left = self.__delete(curr.left, key)
        elif key > curr.key:
            curr.right = self.__delete(curr.right, key)
        else:
            if curr.right is None:
                return curr.left
            if curr.left is None:
                return curr.right
            t = curr
            curr = t.right.min()
            curr.right = t.right.delete_min()
            curr.left = t.left

        return curr

    def find_highest(self, attribute: str, number: int):
        values = []
        stack = []
        curr = self.root

        # Preorder traversal
        while curr or len(stack):
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            values.append(curr.data)
            curr = curr.right

        return sorted(values, key=lambda s: getattr(s, attribute), reverse=True)[:number]
