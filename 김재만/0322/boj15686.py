# 치킨 배달

def check_dist(home, chicken):
    '''
    home : home_list
    chicken : comb 함수에서 구한 뽑힌 chicken 집 리스트
    '''
    # 집을 기준으로 최소 거리 하나씩 구하기
    ans = 0
    for home_x, home_y in home:
        chicken_distance = 99999999
        for chicken_x, chicken_y in chicken:
            chicken_distance = min(chicken_distance, abs(home_x-chicken_x)+abs(home_y-chicken_y))
        ans += chicken_distance
    return ans


def comb(home, m):
    global result
    
    if len(comb_list) == m:
        # 살아남을 치킨집을 골랐다면?
        # 여기에서 이제 계산 시작 [치킨집 - 집] 사이의 최소 거리구하기
        min_v = check_dist(home,comb_list)
        result = min(result, min_v)
        return
    
    start = chicken_list.index(comb_list[-1]) if comb_list else 0
    for i in range(start,len(chicken_list)):
        if not visited[i]:
            visited[i] = 1
            comb_list.append(chicken_list[i])
            comb(home_list,m)
            comb_list.pop()
            visited[i] = 0



n, m = map(int,input().split())
c_map = []
chicken_list = []
home_list = []
comb_list = []

result = 999999999999

for i in range(n):
    line = list(map(int,input().split()))
    c_map.append(line[:])
    for j in range(len(line)):
        # 입력 받으면서 치킨집 위치, 집 위치 알아내기
        if line[j] == 2:
            chicken_list.append((i,j))
        elif line[j] == 1:
            home_list.append((i,j))

visited = [0] * len(chicken_list)
comb(home_list,m)
print(result)
