from collections import deque


def solution(cacheSize, cities):
    cities = deque(cities)
    caches = []
    tm = 0
    if cacheSize == 0:
        return 5 * len(cities)
    while cities:
        now_city = cities.popleft().lower()

        if len(caches) < cacheSize:
            for i in range(len(caches)):
                if now_city == caches[i]:
                    caches.pop(i)
                    tm += 1
                    break
            else:
                tm += 5
            caches.append(now_city)
        else:
            for i in range(len(caches)):
                if now_city == caches[i]:
                    caches.pop(i)
                    tm += 1
                    break
            else:
                tm += 5
                caches.pop(0)
            caches.append(now_city)

    answer = tm
    return answer