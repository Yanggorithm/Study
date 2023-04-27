"""
-1 : 블랙홀
0 : 빈공간
1~5 : 블록
6~10 : 웜홀

핀볼이 출발위치로 돌아오거나 블랙홀에 빠지면 끝남.

들어오는 방향:
0, 1, 2, 3

진행방향:
1: 1, 3, 0, 2
2: 3, 0, 1, 2
3: 2, 0, 3, 1
4: 1, 2, 3, 0
5: 1, 0, 3, 2
"""
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

direction = [
    [],
    [1, 3, 0, 2],
    [3, 0, 1, 2],
    [2, 0, 3, 1],
    [1, 2, 3, 0],
    [1, 0, 3, 2]
]
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    warmhole = [0,0,0,0,0,0,[],[],[],[],[]]
    for i in range(n):
        t = list(map(int, input().split()))
        arr.append(t)
        
        for j in range(n):
            if t[j] > 5:
                warmhole[t[j]].append((i, j))

    ans = 0     

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                for d in range(4):
                    cnt = 0
                    q = [(i, j)]

                    while q:
                        ci, cj = q.pop()
                        ni, nj = ci+dx[d], cj+dy[d]
                        if (ni, nj) == (i, j):
                            break

                        if 0 <= ni < n and 0 <= nj < n:
                            if arr[ni][nj] == 0:
                                q.append((ni, nj))
                            elif arr[ni][nj] == -1:
                                break
                            elif 6 <= arr[ni][nj] <= 10:
                                if warmhole[arr[ni][nj]].index((ni, nj)):
                                    q.append((warmhole[arr[ni][nj]][0]))
                                else:
                                    q.append((warmhole[arr[ni][nj]][1]))
                            else:
                                cnt += 1
                                q.append((ni, nj))
                                d = direction[arr[ni][nj]][d]                  
                        else:
                            cnt = cnt*2 + 1
                            break
                    
                    ans = max(ans, cnt)
    
    print(f"#{tc} {ans}")
