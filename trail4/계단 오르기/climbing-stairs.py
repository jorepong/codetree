n = int(input())

memo = [-1] * (n + 1)

def solution(num):
    if memo[num] != -1:
        return memo[num]

    if num == 1:
        return 0
    elif num == 2 or num == 3:
        return 1
    
    memo[num] = solution(num - 2) + solution(num - 3)

    return memo[num] % 10007

answer = solution(n)
print(0 if answer == -1 else answer)