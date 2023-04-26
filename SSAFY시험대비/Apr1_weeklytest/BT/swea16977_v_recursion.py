# 전기버스 2
# 완탐으로 풀기
import sys
sys.stdin = open('input.txt','r')


def electronic_bus(now, cnt):
    global result

    # 가지치기
    if cnt >= result:
        return

    # 도착지를 도착~넘어갔다면 계산하자
    if now >= n-1:
        result = min(result, cnt)
        return

    # 현재 위치에서 배터리양으로 갈 수 있는 만큼 가자
    for i in range(n_list[now]):
        electronic_bus(now+i+1, cnt+1)


T = int(input())

for tc in range(1, T + 1):
    n, *n_list = map(int, input().split())
    result = 999999999

    # 계산하자
    electronic_bus(0, 0)
    print(f"#{tc} {result - 1}")
