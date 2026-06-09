n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[-1] * n for _ in range(n)]
dp[0][0] = grid[0][0]

for r in range(n):
    for c in range(n):
        if r == 0 and c == 0:
            continue
        if r == 0:
            dp[r][c] = dp[r][c-1]
        elif c == 0:
            dp[r][c] = dp[r-1][c]
        else:
            dp[r][c] = max(dp[r][c-1], dp[r-1][c])
        dp[r][c] += grid[r][c]

print(dp[n-1][n-1])