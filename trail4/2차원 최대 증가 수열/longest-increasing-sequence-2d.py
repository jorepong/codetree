n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[1] * m for _ in range(n)]

for r in range(1, n):
    for c in range(1, m):
        for ir in range(r):
            for ic in range(c):
                if grid[ir][ic] < grid[r][c]:
                    dp[r][c] = max(dp[r][c], dp[ir][ic] + 1)

answer = max(dp[-1])
for i in range(n):
    answer = max(answer, dp[i][-1])

print(answer)