def goodnum(n: int) -> int:
    MOD = 10**9 + 7
    ep = (n + 1 )// 2
    op = n // 2
    few = power(4, ep, MOD)
    fow = power(5,op, MOD)
    res = (few * fow) % MOD
    print(res)

def power(x, y, mod):
    result = 1
    x = x % mod
    while y > 0:
        if y % 2 == 1:   
            result = (result * x) % mod
        y = y // 2       
        x = (x * x) % mod
    return result

goodnum(4)