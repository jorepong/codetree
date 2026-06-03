n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
answer = 0

def move(cr, cc, score, path):
    global answer
    
    answer = max(answer, score)

    if 9 - num[cr][cc] + score <= answer:
        return

    dr, dc = dirs[move_dir[cr][cc] - 1]
    i = 1
    while True:
        nr, nc = cr + (dr * i), cc + (dc * i)
        if 0 <= nr < n and 0 <= nc < n:
            if num[cr][cc] < num[nr][nc]:
                path.append((nr, nc))
                move(nr, nc, score + 1, path)
        else:
            break
        i += 1

move(r - 1, c - 1, 0, [(r-1, c-1)])
print(answer)
