# [3] 선택받은 사람, 계단의 번호
def how_time(lstAB, stairsAB):
    # 계단의 위치
    sr, sc = stairsAB
    # 계단수
    tm = building[sr][sc]

    # 어차피 리스트가 비어있으면 0이니까 0을 반환
    if len(lstAB) == 0:
        return 0

    # 선착순으로 오는 사람먼저 계산해주기 위한 리스트
    waiting = []

    # 사람과 계단 까지의 거리를 계산해서 리스트에 넣어줌.
    for r, c in lstAB:
        tmp = abs(sr-r) + abs(sc-c)
        waiting.append(tmp)
    # 정렬
    waiting.sort()

    # 3명 이하면 마지막에 온 사람이 제일 오래 걸리니까 마지막 사람만 tm을 더해주고 리턴
    if len(waiting) <= 3:
        return waiting[-1] + tm
    else:
        # 3명 이상이면 우선 1명 2명 3명을 먼저 tm을 더해주고
        waiting[0] = waiting[0] + tm
        waiting[1] = waiting[1] + tm
        waiting[2] = waiting[2] + tm

        # dp 형식으로 계산해서 마지막 사람을 리턴
        for i in range(3, len(waiting)):
            if waiting[i] < waiting[i-3]:
                waiting[i] = waiting[i-3] + tm
            else:
                waiting[i] += tm
        return waiting[-1]

# [2] 두 그룹으로 나누는 함수
def dfs(idx, A, B):
    global min_tm
    if idx == len(people):
        # 여기서 계산
        tm = max(how_time(A, stairs[0]), how_time(B, stairs[1]))
        min_tm = min(tm, min_tm)
        return

    # A에 넣고 B에 넣고
    dfs(idx+1, A+[people[idx]], B)
    dfs(idx+1, A, B+[people[idx]])


# [1] 사람, 계단, 빌딩을 받아준다.
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    building, stairs, people = [], [], []
    for r in range(N):
        building.append(list(map(int, input().split())))
        for c in range(N):
            if building[r][c] == 1:
                people.append((r, c))
            elif building[r][c] >= 2:
                stairs.append((r, c))
    min_tm = 10**9

    # 두 그룹으로 나누기
    dfs(0, [], [])

    # 마지막에 1더해주기
    # 계단에서 1분 있다가 가기 때문에
    print(f"#{tc} {min_tm+1}")