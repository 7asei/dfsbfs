import random
from collections import defaultdict

n = 3  # dane wejściowe
m = 3

i = random.randint(1, n)
j = random.randint(1, m)

graph = {
    'S': [1, 1, random.randint(1, 10)],
    'G': [4, 5, random.randint(1, 10)]  # parametry
}

if i < n:
    graph['A'] = [i + 1, j, random.randint(1, 10)]

if i > 1:
    graph['B'] = [i - 1, random.randint(1, 10)]

if j < m:
    graph['C'] = [i, j + 1, random.randint(1, 10)]

if j > 1:
    graph['D'] = [i, j - 1, random.randint(1, 10)]  # wymagania dla połączeń

print(graph)

visited = []  # odwiedzone
queue = []  # kolejka


def bfs(visited, graph, node):  # funkcja dla bfs
    visited.append(node)
    queue.append(node)

    while queue:
        k = queue.pop()
        print(k, end=" ")

        for neighbour in graph:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# dfs

print("BFS")
bfs(visited, graph, 'S')  # wywołanie funkcji

visited = set()  # do trackowania odwiedzonych nodów


def dfs(visited, graph, node):  # funkcja dla dfs
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph:
            dfs(visited, graph, neighbour)


print("\nDFS")
dfs(visited, graph, 'S')

