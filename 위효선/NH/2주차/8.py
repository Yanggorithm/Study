# 프로그래머스 2016년

# from datetime import datetime
# def solution(a, b):
#    answer = datetime(2016, a, b)
#    weekday = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
#    return weekday[answer.weekday()]

def solution(a, b):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = sum(days[1:a]) + b - 1
    weekday = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    return weekday[total%7]