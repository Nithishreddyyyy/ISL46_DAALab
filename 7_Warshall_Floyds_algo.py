#Warshall's Algorithm

def Warshal(a, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if a[i][k] == 1 and a[k][j] == 1:
                    a[i][j] = 1

if __name__ == "__main__":
    n = 4
    a = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ]

    Warshal(a, n)

    print("-----Transitive Closure Matrix-----")
    for row in a:
        print(row)
