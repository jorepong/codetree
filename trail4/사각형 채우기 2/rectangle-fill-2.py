n = int(input())

dp = [1, 3]

for _ in range(2, n + 1):
    dp.append(dp[-1] + dp[-2] * 2)

print(dp[n-1] % 10007)