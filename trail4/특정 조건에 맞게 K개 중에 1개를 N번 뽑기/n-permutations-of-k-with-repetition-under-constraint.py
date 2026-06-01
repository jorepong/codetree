K, N = map(int, input().split())

# Please write your code here.

answer = []

def solution(pos, path):
    if pos == N:
        answer.append(path[:])
        return

    for n in range(1, K + 1):
        if len(path) < 2 or not (path[-1] == n and path[-2] == n):
            path.append(n)
            solution(pos + 1, path)
            path.pop()

solution(0, [])

for a in answer:
    print(*a)