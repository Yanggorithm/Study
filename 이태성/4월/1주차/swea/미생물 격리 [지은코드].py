from pprint import pprint
from collections import deque

t = int(input())

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
rd = [0, 2, 1, 4, 3]

for tc in range(1, t + 1):
    # 셀의 개수, 격리시간, 군집 개수
    n, m, k = map(int, input().split())
    arr = [[[] for _ in range(n)] for _ in range(n)]
    # print(arr)

    microbe = {}
    # 미생물 군집 입력
    for i in range(1, k + 1):
        # [군집 세로위치, 가로위치, 미생물 수, 이동방향]
        t = list(map(int, input().split()))
        microbe[i] = t
        # 현재 위치 표시
        arr[t[0]][t[1]].append(i)

    # 시간
    time = 0
    while time != m:
        # 군집 반복
        for i in range(1, k + 1):
            # 군집이 있으면
            if microbe[i] != 0:
                # 현재 군집 정보
                ci, cj, cm, d = microbe.get(i)
                # 이동
                ni, nj = ci + dx[d], cj + dy[d]

                # 위치 확인
                if 0 < ni < n - 1 and 0 < nj < n - 1:
                    microbe[i] = [ni, nj, cm, d]
                # 이동한 위치가 가장자리일 경우
                elif ni == 0 or nj == 0 or ni == n - 1 or nj == n - 1:
                    # 현재 군집의 위치, 미생물수, 방향 변경
                    if cm // 2:
                        microbe[i] = [ni, nj, cm // 2, rd[d]]
                    else:
                        microbe[i] = []

                # 이동 좌표 저장
                if 0 <= ni < n - 1 and 0 <= nj < n - 1 and microbe[i] != 0:
                    arr[ni][nj].append(i)
                # 이전에 있던 위치 정보 삭제
                if arr[ci][cj].count(i):
                    arr[ci][cj].remove(i)

        # 군집 집단을 모두 이동시키고 나서 한군데로 모인 지점 합쳐주기
        for ai in range(n):
            for aj in range(n):
                if len(arr[ai][aj]) > 1:
                    maxV, sumV, nd, prev = 0, 0, 0, 0
                    for ak in arr[ai][aj]:
                        prev = ak
                        sumV += microbe[prev][2]
                        if maxV < microbe[prev][2]:
                            maxV = microbe[prev][2]
                            nd = microbe[prev][3]
                            microbe[prev] = 0
                    arr[ai][aj] = [prev]
                    microbe[prev] = [ai, aj, sumV, nd]

        time += 1
    ans = 0
    # print(microbe)

    for m in microbe.values():
        if m:
            ans += m[2]

    print(f"#{tc} {ans}")