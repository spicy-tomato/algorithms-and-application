class Heap:
    def __init__(self) -> None:
        self.queue = [None]

    def __swap(self, i: int, j: int) -> None:
        Heap.__s_swap(self.queue, i, j)

    @staticmethod
    def __s_swap(arr: list, i: int, j: int) -> None:
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    def __swim(self, k: int) -> None:
        while k > 1 and self.queue[k // 2] < self.queue[k]:
            Heap.__s_swap(self.queue, k // 2, k)
            k = k // 2

    def __sink(self, k: int) -> None:
        Heap.__s_sink(self.queue, k, self.size())

    @staticmethod
    def __s_sink(arr: list, k: int, n: int):
        while 2 * k <= n:
            j = 2 * k
            if j < n and arr[j] < arr[j + 1]:
                j += 1

            if arr[k] >= arr[j]:
                break

            Heap.__s_swap(arr, k, j)
            k = j

    def empty(self) -> bool:
        return len(self.queue) <= 1

    def size(self) -> int:
        return len(self.queue) - 1

    def insert(self, v) -> None:
        self.queue.append(v)
        self.__swim(self.size())

    def remove(self):
        if self.empty():
            return None

        max_value = self.queue[1]
        self.__swap(1, self.size())
        self.queue.pop()
        self.__sink(1)

        return max_value

    def max(self):
        return None if self.empty() else self.queue[1]

    @staticmethod
    def sort(arr: list) -> None:
        n = len(arr)
        arr.insert(0, None)

        for k in range(n // 2, 0, -1):
            Heap.__s_sink(arr, k, n)

        while n > 1:
            Heap.__s_swap(arr, 1, n)
            n -= 1
            Heap.__s_sink(arr, 1, n)

        arr.pop(0)
