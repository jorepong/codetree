n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[float('inf')] * n for _ in range(n)]

for r in range(n):
    for c in range(n - 1, -1, -1):
        dp[r][c] = grid[r][c]

        if r > 0 and c < n - 1:
            dp[r][c] += min(dp[r-1][c], dp[r][c+1])
        elif r > 0:
            dp[r][c] += dp[r-1][c]
        elif c < n - 1:
            dp[r][c] += dp[r][c+1]

print(dp[n-1][0])