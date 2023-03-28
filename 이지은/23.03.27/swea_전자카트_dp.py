t = int(input())

def solve(now, e_sum):
    global minV

    # 지금까지 구한 에너지의 합이 내가 알고 있는 최소값보다 더 크면 더이상 진행할 필요가 없다.
    # 이후에 진행해봤자 합이 

for tc in range(1, t+1):
    n = int(input())
    battery = [list(map(int, input().split())) for _ in range(n)]

    # 각 방은 1번만 방문해야 되니까 방문체크
    visited = [0] * n

    # 첫번째 방은 출발시 방문했다고 처리
    visited[0] = 1

    minV = 9999999

    solve(0, 0)
    print(f"#{tc} {minV}")



    