from collections import deque

def solution(cacheSize, cities):

    if cacheSize == 0:
        return 5*len(cities)
    # 0 <= cacheSize <= 30
#     cities : 문자열 배열, 최대 도시 수는 100,000
    answer = 0
    cities = deque(cities)
    lst = []
    
    while cities:
        print(lst)
        tmp = cities.popleft().lower()
        if tmp in lst:
            lst.pop(lst.index(tmp))
            lst.append(tmp)
            answer += 1
        else:
            answer += 5
            if len(lst) == cacheSize:
                lst = lst[1:]
                lst.append(tmp)
            else:
                lst.append(tmp)
    return answer

