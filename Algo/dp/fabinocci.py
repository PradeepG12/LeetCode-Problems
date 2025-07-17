# Tabluation
def fabinocciTabu(n):
    dp = [0,1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
# print(fabinocciTabu(15))

n = 7
# memoization
def fabinocciMemo(n):
    if n <= 1:
        return n
    if dp[n] == -1:
        dp[n] = fabinocciMemo(n-2) + fabinocciMemo(n-1)
    return dp[n]
dp = [-1] * (n+1)
print(fabinocciMemo(n))