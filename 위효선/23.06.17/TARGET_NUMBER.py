# 프로그래머스 Lv.2 타겟넘버

def solution(numbers, target):
    answer = 0

    def func(n,s):

        nonlocal answer

        if n == len(numbers):
            if s == target:
                answer += 1
            return
    
        func(n+1, s+numbers[n])
        func(n+1, s-numbers[n])
    
    func(0,0)
    return answer