n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')
dp = [[INF] * n for _ in range(n)]

dp[0][n - 1] = grid[0][n - 1]

for r in range(n):
    for c in range(n - 1, -1, -1):
        if r == 0 and c == n - 1:
            continue

        if r > 0:
            dp[r][c] = min(dp[r][c], dp[r - 1][c] + grid[r][c])

        if c < n - 1:
            dp[r][c] = min(dp[r][c], dp[r][c + 1] + grid[r][c])

print(dp[n - 1][0])