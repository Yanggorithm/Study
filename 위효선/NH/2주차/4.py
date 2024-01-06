# 프로그래머스 카드 뭉치
def solution(cards1, cards2, goal):
    a = b = 0
    n, m = len(cards1), len(cards2)
    for word in goal:
        if a < n and cards1[a] == word:
            a += 1
        elif b < m and cards2[b] == word:
            b += 1
        else:
            return 'No'
    return 'Yes'