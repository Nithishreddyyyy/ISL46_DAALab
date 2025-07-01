N = 4   # Number of items
W = 8   # Capacity of the bag

def knapsack(wt, val):
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for w in range(W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], 
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    print(f"Maximum profit = {dp[N][W]}")

# Inputs
weights = [3,4,6,5]
values = [2,3,1,4]

knapsack(weights, values)