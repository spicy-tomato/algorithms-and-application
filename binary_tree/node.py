class Node:
    def __init__(self, key=None, data=None, parent=None):
        self.key = key
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def min(self):
        if self.left:
            return self.left.min()
        return self

    def delete_min(self):
        if self.left is None:
            return self.right
        self.left = self.left.delete_min()
        return self
