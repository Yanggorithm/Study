import sys
sys.stdin = open('input.txt', 'r')

'''
가장 높은 곳에서 시작
높은 지형에서 낮은 지형으로
딱 한 곳, 최대 k 만큼 깎기 가능
'''
def dfs(sx, sy, changed_map, cnt):
    global result

    result = max(result, cnt)

    for d in range(4):
        now_height = changed_map[sx][sy]
        nx = sx + dx[d]
        ny = sy + dy[d]

        # 만약 갈 수 있다면 다음 위치로
        if 0 <= nx < n and 0 <= ny < n and changed_map[nx][ny] < now_height:
            dfs(nx, ny, changed_map, cnt + 1)

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    m_map = []
    top_list = []
    max_h = 0
    result = 0

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(n):
        a = list(map(int, input().split()))
        max_h = max(max_h, max(a))
        m_map.append(a)

    for i in range(n):
        for j in range(n):
            if m_map[i][j] == max_h:
                top_list.append((i, j))

    for x, y in top_list:
        for i in range(n):
            for j in range(n):
                for depth in range(1, k + 1):
                    m_map[i][j] -= depth
                    dfs(x, y, m_map, 1)
                    m_map[i][j] += depth

    print(f'#{tc} {result}')