n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
dp = [-1] * n
dp[0] = 1

for i in range(1, n):
    max_count = 0
    for j in range(i):
        if m[j] < m[i] and dp[j] > max_count:
            max_count = dp[j]
    dp[i] = max_count + 1

print(max(dp))