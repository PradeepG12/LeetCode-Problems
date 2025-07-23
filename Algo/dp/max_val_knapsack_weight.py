data = [
    {"W":50, "val":[60, 100, 120], "wt":[10, 20, 30]},
    {"W":8, "val":[10, 40, 50, 70], "wt":[1, 3, 4, 5],},
    {"W":4, "val":[1, 2, 3], "wt":[4, 5, 1]},
    {"W":3, "val":[1, 2, 3], "wt":[4, 5, 6]},
]
def knapsackBrute(wt, val, W):
    n = len(val)
    maxi = 0
    for i in range(n):
        weight = wt[i]
        tot = val[i]
        if weight <= W:
            maxi = max(maxi, tot)
        else: continue
        for j in range(i+1, n):
            if weight < W:
                weight += wt[j]
                tot += val[j]
            if weight > W:
                break
            maxi = max(maxi, tot)
    return maxi

def knapsackBetter(wt, val, W):
    n = len(wt)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w-wt[i-1]])
    return dp[n][W]

