from collections import deque
import sys
sys.setrecursionlimit(10**9)

def distance(sr, sc, ar, ac):
    return abs(sr - ar) + abs(sc - ac)

def total_distance(arr):
    td = distance(company_r, company_c, arr[0][0], arr[0][1]) + distance(home_r, home_c, arr[-1][0], arr[-1][1])
    for i in range(N-1):
        td += distance(arr[i][0], arr[i][1], arr[i+1][0], arr[i+1][1])
    return td

def dfs(stack):
    global min_distance
    if len(stack) == N:
        min_distance = min(total_distance(stack), min_distance)
        return
    for loc in location_clients:
        if loc not in stack:
            new_stack = stack.copy()
            new_stack.append(loc)
            dfs(new_stack)

T = int(input())
for tc in range(1, T+1):
    # 2 <= N <= 10
    N = int(input())
    min_distance = 200*10000
    clients = list(map(int, input().split()))
    location_clients = deque()
    company_r, company_c = clients[0], clients[1]
    home_r, home_c = clients[2], clients[3]
    for i in range(2, N+2):
        location_clients.append((clients[i*2], clients[i*2+1]))
    dfs([])
    print(f"#{tc} {min_distance}")