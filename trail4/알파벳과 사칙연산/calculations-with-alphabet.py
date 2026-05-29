from collections import defaultdict

expression = input()
alphas = set()

for i in range(len(expression)):
    if i % 2 == 0:
        alphas.add(expression[i])

alphas = list(alphas)
alpha_map = defaultdict(int)
answer = -float('inf')

def calculate():
    global answer
    result = alpha_map[expression[0]]
    for j in range(2, len(expression), 2):
        if expression[j-1] == '+':
            result += alpha_map[expression[j]]
        elif expression[j-1] == '-':
            result -= alpha_map[expression[j]]
        else:
            result *= alpha_map[expression[j]]
    answer = max(answer, result)

def select(pos):
    if pos == len(alphas):
        calculate()
        return
    
    for i in range(1, 5):
        alpha_map[alphas[pos]] = i
        select(pos + 1)

select(0)
print(answer)