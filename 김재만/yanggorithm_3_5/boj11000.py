# 강의실 배정
import sys
input = sys.stdin.readline
import heapq

def search_class(h):
    global ans
    
    end = 0
    tmp = []
    while h:
        # 하나 뺴고 앞에 값이랑 비교 무조건 강의실 하나씩만 증가
        e, s = heapq.heappop(h)
        # 앞 강의가 끝나는 시간 <= 뒷 강의 시작 시간 이면 강의실 증가 필요 x
        if end <= s:
            end = e
            if tmp:
                search_class(tmp)
        # 앞 강의가 끝나는 시간 > 뒷 강의 시작 시간 이면 강의실 증가 필요
        else:
            ans += 1
            heapq.heappush(tmp, (e, s))


n = int(input())

hq = []

ans = 1

for _ in range(n):
    s, t = map(int,input().split())
    heapq.heappush(hq, (t, s))
    
search_class(hq)
    
print(ans)