# 프로그래머스 과일 장수

def solution(k, m, score):
    score.sort(reverse = True)
    r = 0
    n = len(score)
    for i in range(m-1, n, m):
        r += score[i] * m
    return r