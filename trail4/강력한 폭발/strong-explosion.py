n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bombs = []
for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            bombs.append((r, c))

answer = 0
explosion_grid = [[0] * n for _ in range(n)]

bomb_type = [
    [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
    [(-1, 0), (1, 0), (0, 0), (0, 1), (0, -1)],
    [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]
]

def explode(idx):
    global answer
    if idx >= len(bombs):
        explosion_blocks = 0
        for r in range(n):
            for c in range(n):
                if explosion_grid[r][c] > 0:
                    explosion_blocks += 1
        answer = max(answer, explosion_blocks)
        return
    
    for type in range(3):
        for dr, dc in bomb_type[type]:
            nr, nc = bombs[idx][0] + dr, bombs[idx][1] + dc
            if 0 <= nr < n and 0 <= nc < n:
                explosion_grid[nr][nc] += 1
        explode(idx + 1)
        for dr, dc in bomb_type[type]:
            nr, nc = bombs[idx][0] + dr, bombs[idx][1] + dc
            if 0 <= nr < n and 0 <= nc < n:
                explosion_grid[nr][nc] -= 1
        
explode(0)
print(answer)