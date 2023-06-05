p = { 0:(),
      1:((-1, 0), (1, 0), (0, -1), (0, 1)),
      2:((-1, 0), (1, 0)),
      3:((0, -1), (0, 1)),
      4:((-1, 0), (0, 1)),
      5:((1, 0), (0, 1)),
      6:((1, 0), (0, -1)),
      7:((-1, 0), (0, -1)) }

t = int(input())
for tc in range(1, t+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [[0] * m for _ in range(n)]

    # 맨홀 위치 좌표 (r, c)
    v[r][c] = 1
    q = [(r, c)]

    # 이동 가능한 장소 개수 세기
    cnt = 1    # 시작 지점 + 1

    while q:
        si, sj = q.pop(0)
        for di, dj in p[arr[si][sj]]:
            ni, nj = si + di, sj + dj

            # 유효성 검사, 방문하지 않았다면 확인 해보기
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0:

                # 반대 방향 있는지 확인
                if (-di, -dj) in p[arr[ni][nj]]:
                    q.append((ni, nj))

                    # 기존 값에 + 1 한 값 저장하기
                    v[ni][nj] = v[si][sj] + 1

                    # 제한 시간(l) 보다 작거나 같다면 카운팅
                    if v[ni][nj] <= l:
                        cnt += 1

    print(f'#{tc} {cnt}')