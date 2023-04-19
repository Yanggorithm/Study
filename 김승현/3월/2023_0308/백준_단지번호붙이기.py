from collections import deque

N = int(input())

house = [list(map(int, input())) for _ in range(N)]
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            cnt = 1
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            
            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    
                    if 0 <= nx < N and 0 <= ny < N and house[nx][ny] != 0 and not visited[nx][ny]:
                        house[nx][ny] = 0
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        cnt += 1
            
            
            result.append(cnt)         
  
result.sort()
len_re = len(result)
print(len_re)
for i in range(len_re):
    print(result[i])