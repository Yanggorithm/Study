# python 시간초과, pypy 통과
import sys
from collections import deque

r, c = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]

# 0, 0 에 말
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 이전에 나온 알파벳이 있는 칸은 이동할 수 없음
# 지나올 수 있는 최대칸, 처음 시작 포함

visited = [[0]*c for _ in range(r)]
alphabet = [0] * 26
alphabet[ord(board[0][0])-65] = 1
visited[0][0] = 1

stack = deque([(0,0)])

maxV = 1
def solve(stack):
    global maxV

    while stack:
        ci, cj = stack.popleft()
        for d in range(4):
            ni, nj = ci+dx[d], cj+dy[d]
            
            if 0 <= ni < r and 0 <= nj < c and alphabet[ord(board[ni][nj])-65] == 0:
                o = ord(board[ni][nj])-65
                # for i in range(r):
                #     print(" ".join(map(str, visited[i])))
                # print()
                alphabet[o] = 1
                visited[ni][nj] = visited[ci][cj] + 1
                stack.append((ni, nj))
                if visited[ni][nj] > maxV:
                    maxV = visited[ni][nj]

                solve(stack)
                alphabet[o] = 0
            
# 문제점 : 같은 거리에 있는 다른 장소의 알파벳이 같을 경우
# 해결책 : 1. dfs로 갔다가 막히면 다시 돌아온다.
#          2. backtracking으로 해당 방향으로 간 경우와 안간 경우를 나눈다.

solve(stack)
print(maxV)

