import sys
from collections import deque

# 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(4)]
fish = [[] for _ in range(4)]
xy = [0] * 17
maxV = 0

for i in range(4):
    for j in range(4):
        fish[i].append([arr[i][j*2], arr[i][j*2+1]-1])
        xy[arr[i][j*2]] = (i, j)

xy[arr[0][0]] = 0
# 상어가 0,0 자리에 들어간다.
# 물고기의 이동이 모두 끝나면 상어가 이동한다.
# 번호가 작은 물고기부터 순서대로 이동
# 물고기는 한칸 이동할 수 있음
# 이동할 수 있는 칸 : 빈 칸, 다른 물고기가 있는 칸
# 이동할 수 없는 칸 : 상어가 있거나 공간의 경계를 넘는 칸
# 이동할 수 있는 칸이 나올 때까지 회전
# 8방향 모두 이동할 수 없으면 이동을 멈춤
# 이동할 때는 해당 칸 물고기와 위치를 바꿈.

# 물고기 이동
def fish_move():
    for f in range(1, 17):
        # print(f)
        if xy[f] == 0: continue
        else:
            cnt = 0
            while True:
                if cnt == 7:
                    break
                ci, cj = xy[f][0], xy[f][1]
                # print(ci, cj)
                # print(fish[ci][cj])
                ni, nj = ci + dx[fish[ci][cj][1]], cj + dy[fish[ci][cj][1]]
                if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) != (0, 0):
                    fish[ni][nj], fish[ci][cj] = fish[ci][cj], fish[ni][nj]
                    xy[f] = (ni, nj)
                    xy[fish[ci][cj][0]] = (ci, cj)
                    break
                else:
                    fish[ci][cj][1] = (fish[ci][cj][1] + 1) % 8
                    # print(fish[ci][cj])
                    cnt += 1
                    # # 디버깅
                    # for i in range(4):
                    #     for j in range(4):
                    #         print(fish[i][j], end=" ")
                    #     print()
                    # print("-------------------")

# 상어가 먹을 수 있는 물고기 번호 합의 최대값
# 물고기가 없으면 이동할 수 없음.
# 물고기를 먹고 해당 물고기의 이동 방향을 가지게 됨.
# 이동하는 중에는 물고기를 먹을 수 없음.
q = deque([(0,0)])
lastD = 0

def shark_move(eat, q):
    global maxV, lastD
    
    while q:        
        ci, cj = q.pop()
        for d in range(1,4):
            # print("방향: ", fish[ci][cj][1])
            # print("현 좌표 : ", ci, cj)
            ni, nj = ci + d*dx[fish[ci][cj][1]], cj + d*dy[fish[ci][cj][1]]
            # print("새 좌표 : ", ni, nj)
            if 0 <= ni < 4 and 0 <= nj < 4 and xy[fish[ni][nj][0]] != 0:
                q.append((ni, nj))
                tmp = xy[fish[ni][nj][0]]
                fish[0][0][1] = fish[ni][nj][1]
                xy[fish[ni][nj][0]] = 0
                # print("먹은 물고기 : " , eat+fish[ni][nj][0])
                if maxV < eat+fish[ni][nj][0]:
                    maxV = eat+fish[ni][nj][0]
                    lastD = fish[ni][nj][1]
                shark_move(eat+fish[ni][nj][0], q)
                xy[fish[ni][nj][0]] = tmp

# 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
# 0   1     2   3    4     5   6    7

fish_move()
shark_move(arr[0][0], q)
fish[0][0][1] = lastD

# print(lastD)
# print(maxV)

# # 디버깅
# for i in range(4):
#     for j in range(4):
#         print(fish[i][j], end=" ")
#     print()
# print("====================")
        
    

