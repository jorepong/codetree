N = int(input())

memo = [-1] * (N + 1)

def fib(n):
    if memo[n] != -1:
        return memo[n]
    elif n <= 2:
        memo[n] = 1
    else:
        memo[n] = fib(n-1) + fib(n-2)
    
    return memo[n]

print(fib(N))