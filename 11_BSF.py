# Breadth-First Search (BFS)

def bfs(u):
    queue = [u]
    visited[u] = 1
    while queue:
        current = queue.pop(0)
        print(current)
        for v in range(n):
            if visited[v] == 0 and graph[current][v] == 1:
                queue.append(v)
                visited[v] = 1

if __name__ == "__main__":
    global visited, n, graph

    graph = [
        [0, 1, 1, 0],  # 0 → 1, 2
        [0, 0, 0, 1],  # 1 → 3
        [0, 0, 0, 0],  # 2 → none
        [0, 0, 0, 0]   # 3 → none
    ]


    n = len(graph)
    visited = [0] * n
    source = 0

    print("Adjacency Matrix:")
    for row in graph:
        print(row)

    print("\nBFS Traversal Order:")
    bfs(source)