N = int(input())

memo = [-1] * (N + 1)
memo[1] = 1
memo[2] = 1

def fib(n):
    if memo[n] != -1:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
    
    return memo[n]

print(fib(N))