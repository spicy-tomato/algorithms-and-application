class Graph:
    def __init__(self, size: int):
        self.vertices = [[] for _ in range(size)]

    def link(self, source: int, destination: int):
        self.vertices[source].append(destination)

    def sort(self):
        for vertex in self.vertices:
            sorted(vertex)

    def bfs_from(self, index) -> []:
        return self.__bfs([], [index])

    def __bfs(self, visited: [], stack: []) -> []:
        while len(stack) > 0:
            current = stack.pop(0)
            if index_of(visited, current) == -1:
                visited.append(current)

                for vertex in self.vertices[current]:
                    if index_of(visited, vertex) == -1:
                        stack.append(vertex)

                self.__bfs(visited, stack)
                return visited

    def dfs_from(self, index) -> []:
        return self.__dfs([], index)

    def __dfs(self, visited: [], current: int) -> []:
        if index_of(visited, current) == -1:
            visited.append(current)

            for vertex in self.vertices[current]:
                if index_of(visited, vertex) == -1:
                    self.__dfs(visited, vertex)
            return visited


def index_of(array: [], element) -> int:
    try:
        return array.index(element)
    except ValueError:
        return -1
