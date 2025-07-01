#Dijkstra's Algorithm 
visited = []
dist = []

def dijkstra(graph, n, source):
    global visited, dist
    INF = 999
    visited = [0] * n
    dist = [INF] * n
    dist[source] = 0
    for _ in range(n):
        min_val = INF
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_val:
                min_val = dist[i]
                u = i
                
        if u == -1:     #for marking node as visited
            break  # no more reachable nodes
        visited[u] = 1
        
        
        for v in range(n):
            if not visited[v] and graph[u][v] != INF and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

if __name__ == "__main__":
    graph = [
        [0, 3, 999, 7, 999],
        [3, 0, 4, 2, 999],
        [999, 4, 0, 5, 6],
        [7, 2, 5, 0, 4],
        [999, 999, 6, 4, 0]
    ]
    n = len(graph)
    source = int(input("Enter source node= "))
    print("----Weight Matrix----")
    for row in graph:
        print(row)

    dijkstra(graph, n, source)
    print("Shortest path from source =", source)
    for i in range(n):
        print(f"{source} ---> {i} ==== {dist[i]}" if dist[i]!=999 else "not found")