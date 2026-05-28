n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

lines = []
for i in range(n):
    lines.append((x1[i], x2[i]))

lines.sort(key=lambda x: (x[1], -x[0]))

answer = 0
for i in range(n):
    if i > 0 :
        if lines[i][0] > lines[i - 1][1]:
            answer += 1
    else:
        answer += 1

print(answer)

# Please write your code here.
