from heap import Heap


class PriorityQueue:
    def __init__(self) -> None:
        self.heap = Heap()

    def empty(self) -> bool:
        return self.heap.empty()

    def top(self):
        return self.heap.max()

    def push(self, v):
        self.heap.insert(v)

    def pop(self) -> None:
        self.heap.remove()
