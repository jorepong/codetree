n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * n for _ in range(n)]

def dfs(r, c):
    if dp[r][c] != -1:
        return dp[r][c]

    max_num = 1
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and grid[r][c] > grid[nr][nc]:
            max_num = max(max_num, dfs(nr, nc) + 1)
    
    dp[r][c] = max_num
    return dp[r][c]

answer = 0

for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)