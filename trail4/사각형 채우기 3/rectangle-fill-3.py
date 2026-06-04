n = int(input())

# Please write your code here.


# 2 * 1 : 2가지
# 2 * 2 : 7가지
# 2 * 3 : dp[n-1] * 2 + dp[n-2] * 3 / 12가지 + 6가지 = 18가지 

dp = [2, 7]

for _ in range(3, n + 1):
    dp.append(dp[-1] * 2 + dp[-2] * 3 + 2)

print(dp[n-1] % 1000000007)