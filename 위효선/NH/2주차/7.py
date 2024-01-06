# 프로그래머스 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    prize = [6, 6, 5, 4, 3, 2, 1]
    best, worst = 6, 0
    
    luck = lottos.count(0)
    worst = len(set(lottos) & set(win_nums))
    best = worst + luck
    
    return [prize[best], prize[worst]]