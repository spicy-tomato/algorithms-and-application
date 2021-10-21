from graph import Graph


def print_vertices(element: [], pre='') -> None:
    print(pre, end='')
    print('->'.join([str(e) for e in element]))


g = Graph(7)

g.link(0, 1)
g.link(0, 2)
g.link(0, 3)
g.link(1, 3)
g.link(1, 4)
g.link(2, 5)
g.link(3, 2)
g.link(3, 5)
g.link(3, 6)
g.link(4, 3)
g.link(4, 6)
g.link(6, 5)

g.sort()

bfs = g.bfs_from(0)
print_vertices(bfs, 'BFS: ')

dfs = g.dfs_from(0)
print_vertices(dfs, 'DFS: ')
