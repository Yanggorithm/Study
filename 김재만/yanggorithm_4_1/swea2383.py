# swea 점심 식사시간

## 풀이중

import sys

sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(lst, K):
    # 리스트 a, b 를 받아서 작은 값(가까운곳) 부터 입구 도착
    # 입구를 큐로 만들어서 빠져나가는것을 구현
    # 입구 1분 대기하므로 1부터 시작
    time = 1
    q = deque(lst)
    # 계단 내려 가는 큐
    sq = deque()
    s_cnt = 0
    
    while q:
        cnt = 0
        num = q[0]
        time += num
        for i in range(len(q)):
            q[i] -= num
            if q[i] == 0:
                cnt += 1
        
        sq_cnt = 0
        for j in range(len(sq)):
            sq[j] -= num
            if sq[j] <= 0:
                sq_cnt += 1
                if s_cnt:
                    sq.append(K)
                    s_cnt -= 1
        
        for _ in range(sq_cnt):
            sq.popleft()
        
        for _ in range(cnt):
            q.popleft()
            # 3명이 넘었다면 기다려야함
            if len(sq) < 3:
                sq.append(K)
            # 대기자는 계단 내려갈 준비
            # 이곳이 문제 발생할 확률이 높음
            else:
                s_cnt += 1
    
    # sq 와 s_cnt 만 계산 해주면 됨
    while sq:
        cnt = 0
        num = sq[0]
        time += num
        for i in range(len(sq)):
            sq[i] -= num
            if sq[i] == 0:
                cnt += 1
                
        for _ in range(cnt):
            sq.popleft()
            if s_cnt:
                sq.append(K)
                s_cnt -= 1
    
    return time


def comb(a, b, start):
    global ans

    if len(a) + len(b) == len(people):
        a_time = bfs(sorted(a), c_map[stairs[0][0]][stairs[0][1]])
        b_time = bfs(sorted(b), c_map[stairs[1][0]][stairs[1][1]])
        result = max(a_time, b_time)
        ans = min(ans, result)
        return

    for idx in range(start, len(people)):
        # 그때 그때 거리를 구해서 넣자
        comb(a+[abs(stairs[0][0] - people[idx][0]) + abs(stairs[0][1] - people[idx][1])], b, idx+1)
        comb(a, b+[abs(stairs[1][0] - people[idx][0]) + abs(stairs[1][1] - people[idx][1])], idx+1)


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    ans = 9999999

    c_map = [list(map(int, input().split())) for _ in range(n)]

    people = []
    stairs = []
    for i in range(n):
        for j in range(n):
            if c_map[i][j] == 1:
                people.append((i, j))
            elif c_map[i][j] > 1:
                stairs.append((i, j))

    visited = [0] * len(people)
    comb([], [], 0)
    print(f"#{tc} {ans}")