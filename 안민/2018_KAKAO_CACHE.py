def solution(cacheSize, cities):
    lst= []
    time=0

    if cacheSize!=0:
        for city in cities:
            if len(lst)<cacheSize and city.upper() not in lst: #초반에 리스트 채우기
                lst.append(city.upper())
                time+=5
            else:
                if city.upper() not in lst: #기존에 없다면 채우기
                    lst.pop(0) #맨앞 빼고
                    lst.append(city.upper()) #최신 걸로 채우기
                    time+=5 #캐치 히트
                else: #리스트에 이미 있다면?
                    lst.pop(lst.index(city.upper())) #이미 있던놈 빼고 새로 들어온 놈으로 위치 업뎃
                    lst.append(city.upper())
                    time+=1
    else:
        time = len(cities)*5 #캐시크기 0인경우
    return time

# cities= ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# cacheSize = 3
# print(solution(cacheSize, cities))