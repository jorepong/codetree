n = int(input())

# Please write your code here.

dp = [1, 0, 0, 0]

for _ in range(n):
    a, b, c, d = dp
    a, b, c, d = 2 * a + b + c + d, a + c, a + b, a
    dp = [a, b, c, d]

print(dp[0])