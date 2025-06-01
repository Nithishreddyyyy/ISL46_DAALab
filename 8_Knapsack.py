def knapsack(W, wt, val, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w - wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    print("Maximum Profit:", dp[n][W])
    print("Selected item indices (0-based): ", end="")
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            print(i-1, end=" ")
            w -= wt[i-1]
    print()

profit = [0,12,10,20,15]
weight = [0,2,1,3,2]
capacity = 50
n = len(profit)

knapsack(capacity, weight, profit, n)
