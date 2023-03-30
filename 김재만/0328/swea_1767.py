# 프로세서 연결하기
# bonus 문제
import sys

sys.stdin = open('input.txt', 'r')


def dfs(idx, m_cnt, ans):
    global max_core
    '''
    :param idx: xy_list 를 가리키는 인덱스
    :param m_cnt: 연결된 멕시노스 갯수
    :param ans: 최종 전선 연결 갯수
    :return:
    '''
    # 가지치기 남은 코어 갯수를 모두 더해도 현재까지 구했던 최대 코어갯수 보다 작다면 더 이상 구할 의미가 없어 종료
    # 백트래킹
    if m_cnt + len_core - idx < max_core:
        return

    if len_core == idx:
        result.append((m_cnt, ans))
        max_core = max(max_core, m_cnt)
        return
    else:
        for d in range(4):
            step = 1
            visit_list = []
            while True:
                nx = xy_list[idx][0] + (dx[d] * step)
                ny = xy_list[idx][1] + (dy[d] * step)
                if 0 <= nx < n and 0 <= ny < n and m_map[nx][ny]:
                    # 범위 안에 있지만 이동 불가능한 지역
                    break
                elif nx < 0 or nx >= n or ny < 0 or ny >= n:
                    # 전원이 연결되었다면
                    # 길 바꿔놓기
                    for vx, vy in visit_list:
                        m_map[vx][vy] = 2
                    # 다음 검사
                    dfs(idx + 1, m_cnt + 1, ans + step - 1)
                    # 길 원위치 시키기
                    for vx, vy in visit_list:
                        m_map[vx][vy] = 0
                    break
                elif 0 <= nx < n and 0 <= ny < n and not m_map[nx][ny]:
                    # 범위 안에 있지만 이동 가능한 지역
                    # 방문 체크리스트에 더해놓고 단계 증가.
                    visit_list.append((nx, ny))
                    step += 1
    # 상하좌우 탐색을 다해봤는데 갈곳이 없을경우 그 멕시노스는 연결 불가로 판단하고 일단 넘어간다.
    dfs(idx + 1, m_cnt, ans)


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    m_map = [list(map(int, input().split())) for _ in range(n)]

    # 검사 대상 찾아 리스트에 넣기
    xy_list = []
    for i in range(n):
        for j in range(n):
            # 외곽에 있으면 굳이 검사할 필요가 없음
            if m_map[i][j] == 1 and i != 0 and j != 0 and i != n - 1 and j != n - 1:
                xy_list.append((i, j))

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    len_core = len(xy_list)
    result = []
    max_core = 0

    dfs(0, 0, 0)
    result.sort(key=lambda x: (-x[0], x[1]))
    print(f"#{tc} {result[0][1]}")
