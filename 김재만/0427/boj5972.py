# 택배 배송
# 다익스트라 풀이중

import sys
import heapq
input = sys.stdin.readline

# def getSmallIndex():
#     min_val = INF
#     for i in range(n+1):
#         if (not visited[i]) and min_val > dp[i]:
#             next = i
#             min_val = dp[i]

#     return next


def dijkstra():
    '''
    start : 시작 인덱스
    getSmallIndex : 방문한 값중 최소값 가져오기 (확정작업)
    '''
    while hq:
        
        distance, start = heapq.heappop(hq)
        
        for i in range(len(adj_list[start])):
            to, value = adj_list[start][i]  # to로 가며 value만큼 가중치를 가짐
            if dp[to] > value + distance:
                dp[to] = value + distance # 더 작은 값이면 값 변경
                heapq.heappush(hq, (dp[to], to))
        
        # 다 돌게 되면 가장 작은 값을 다음 값으로 넣어주기
        # start = getSmallIndex()
    
    return


n, m = map(int, input().split())

INF = 99999999

dp = [INF] * (n+1)
# 1에서 출발
dp[1] = 0
hq = []
heapq.heappush(hq, (0, 1))  # (값, 노드번호)
# 타겟은 n에 있음 
adj_list = [[] for _ in range(n+1)]

for i in range(m):
    A_i, B_i, C_i = map(int, input().split())
    adj_list[A_i].append((B_i, C_i))
    adj_list[B_i].append((A_i, C_i))

dijkstra()
print(dp[n])