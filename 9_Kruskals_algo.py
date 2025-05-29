# Kruskal's Algorithm Implementation
p = []

def parent(x):
    while x != p[x]:
        x = p[x]
    return x

def kruskal(graph, n):
    for i in range(n):
        p.append(i)
    total_cost = 0
    ecount = 0
    while ecount < n - 1:
        minimum = 999
        for i in range(n):
            for j in range(n):
                if i != j and graph[i][j] < minimum:
                    minimum = graph[i][j]
                    u = i
                    v = j
        if parent(u) != parent(v):
            print("connect\t", u, "--->", v, "=", graph[u][v])
            ecount += 1
            p[parent(v)] = parent(u)   # Fixed union step here
            total_cost += graph[u][v]
        graph[u][v] = graph[v][u] = 999
    print("MST total Cost= ", total_cost)

if __name__ == "__main__":
    graph = [
        [0, 30, 40, 999, 999, 999],
        [30, 0, 50, 10, 999, 999],
        [40, 50, 0, 999, 20, 999],
        [999, 10, 999, 0, 60, 80],
        [999, 999, 20, 60, 0, 70],
        [999, 999, 999, 80, 70, 0]
    ]
    n = 6
    print('.....Weight matrix.....')
    for row in graph:
        print(row)
    print(".....MST EDGE.....")
    kruskal(graph, n)
