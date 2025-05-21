def parenthesis(n):
    sol = []
    ans = []

    def backtracking(OC,CC):
        if OC == CC == n:
            ans.append(''.join(sol))
            return
        if OC < n:
            sol.append('(')
            backtracking(OC + 1, CC)
            sol.pop()
        if OC > CC:
            sol.append(')')
            backtracking(OC, CC + 1)
            sol.pop()

    backtracking(0, 0)
    print(sol)
    print(ans)
    return

parenthesis(3)
