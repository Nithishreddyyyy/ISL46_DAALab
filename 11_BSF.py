#Breadth-First-Search 
def bfs(u):
    count = 0
    queue.append(u)
    visited[u] = 1
    while queue:
        u = queue.pop(0)
        count += 1
        print(u)
        for v in range(n):
            if visited[v] == 0 and graph[u][v] == 1:
                queue.append(v)
                visited[v] = 1

if __name__ == "__main__":
    global visited, queue
    visited = [0] * n  # Better initialization
    queue = []         # Reset in case reused
    source = 0
    print("Adjacency Matrix")
    for row in graph:
        print(row)
    print("BFS Order")
    bfs(source)

