# 2018 카카오 블라인드 테스트 1차 - 캐시


from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    cache = deque()
    
    if cacheSize:
        for city in cities:
            city = city.upper()
            # 이미 있는 도시가 들어오려고 한다면?
            for i in range(len(cache)):
                if cache[i] == city:
                    for j in range(i,len(cache)-1):
                        cache[j], cache[j+1] = cache[j+1], cache[j]
                    answer += 1
                    break
            # 새로운 도시가 들어오려고 한다면?
            else:
                # 아직 캐시에 다 차지 않았다면
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                # 만약 캐시에 다 찼다면
                else:
                    cache.popleft()
                    cache.append(city)
                    answer += 5
    else:
        answer = 5 * len(cities)

    return answer