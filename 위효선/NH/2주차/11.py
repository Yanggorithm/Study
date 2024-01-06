# 프로그래머스 체육복

def solution(n, lost, reserve):
    
    n_lost = sorted([ x for x in lost if x not in reserve ])
    n_reserve = sorted([ x for x in reserve if x not in lost ])
    
    for i in n_reserve:
        if i-1 in n_lost:
            n_lost.remove(i-1)
        elif i+1 in n_lost:
            n_lost.remove(i+1)
    
    return n-len(n_lost)