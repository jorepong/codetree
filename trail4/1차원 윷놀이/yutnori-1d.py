n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.

forwards = [1] * k
max_score = 0

def solution(turn):
    global max_score
    if turn == n:
        score = 0
        for i in range(k):
            if forwards[i] >= m:
                score += 1
        max_score = max(max_score, score)
        return

    for player in range(k): # 0 ~ K-1 의 플레이어들
        forwards[player] += nums[turn]
        solution(turn + 1)
        forwards[player] -= nums[turn]
        
solution(0)
print(max_score)