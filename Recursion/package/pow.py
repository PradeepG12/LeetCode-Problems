def Pow(x, n):
    if n == 0:
        return 1.0
    if n < 0:
        x = 1 / x
        n = -n
    if n % 2 == 0:
        return Pow(x * x, n // 2)
    else:
        return x * Pow(x * x, (n-1) // 2)

print(Pow(2.00000,10))