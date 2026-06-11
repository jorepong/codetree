n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1

for r in range(1, n):
    for c in range(1, m):
        for ir in range(r):
            for ic in range(c):
                if grid[ir][ic] < grid[r][c]:
                    dp[r][c] = max(dp[r][c], dp[ir][ic] + 1)

answer = 0
for line in dp:
    answer = max(answer, max(line))

print(answer)