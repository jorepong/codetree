n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

lines = []
for i in range(n):
    lines.append((x1[i], x2[i]))

lines.sort(key=lambda x: (x[1], x[0]))

answer = []
for i in range(n):
    if i > 0 :
        if lines[i][0] > answer[-1][1]:
            answer.append(lines[i])
    else:
        answer.append(lines[i])
print(len(answer))