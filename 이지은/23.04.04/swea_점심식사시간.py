"""
접근방법 : 
1. 사람들을 두그룹으로 나눈다 from itertools import combinations
2. 그룹 별로 각 사람들이 계단까지 도착하는 시간을 구한다.
3. 시간을 늘려가면서, 사람들이 계단에 도착하는 시간과 계단을 다 내려가는 시간을 계산해준다.

"""

from itertools import combinations
from collections import deque

def solve(people, st):
    s = []
    e = deque([])

    for pi, pj in people:
        pt = abs(pi - st[0]) + abs(pj - st[1])
        s.append(pt)
    s.sort()
    s = deque(s)

    time = 0
    cnt = 0

    while s:
        time += 1

        # 이동을 완료했을 경우
        while e and e[0] == time:
            e.popleft()
            cnt -= 1

        while s[0] < time:
            # 계단 이동
            if cnt < 3:
                s.popleft()
                if not s:
                    time += arr[st[0]][st[1]]
                    break

                e.append(time+arr[st[0]][st[1]])
                cnt += 1
            else:
                break
        
        """
        오답 코드
        print('test: ', s[0], time)
        if s[0] > time:
            continue
        
        if cnt < 3:
            s.popleft()
            cnt += 1
            time += arr[st[0]][st[1]]
            e.append(time)
        else:
            if e[-1] > time:
                continue
            else:
                cnt -= 1
        """
    
    return time

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    arr = []
    stairs = []
    people = []

    # 배열 입력
    for i in range(n):
        a = list(map(int, input().split())) 
        arr.append(a)

        for j in range(n):
            # 사람 위치 확인
            if a[j] == 1:
                people.append((i, j))
            # 계단위치 확인
            elif a[j] > 1:
                stairs.append((i, j))
    
    ans = 9999999999
    for i in range(n):
        for group1 in combinations(people, i):
            group2 = list(set(people) - set(group1))

            time1 = solve(group1, stairs[0])
            time2 = solve(group2, stairs[1])
            result = max(time1, time2)
            ans = min(ans, result)

    print(f"#{tc} {ans}")

