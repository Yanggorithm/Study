t = int(input())

def get_result(arr):
    tmp = 0
    for i in range(n-2):
        tmp += battery[arr[i]-1][arr[i+1]-1]
    tmp += (battery[0][arr[0]-1] + battery[arr[n-2]-1][0])
    return tmp
        
def solve(i):
    global minV
    if i == n-2:
        tmp = get_result(arr)
        if tmp < minV:
            minV = tmp
        return
    
    for j in range(i, n-1):
        arr[i], arr[j] = arr[j], arr[i]
        solve(i+1)
        arr[i], arr[j] = arr[j], arr[i]
        

for tc in range(1, t+1):
    n = int(input())
    battery = [list(map(int, input().split())) for _ in range(n)]

    arr = [i for i in range(2, n+1)]
    minV = 999999999
    
    # 1번이 사무실, 사무실 출발, 사무실 도착
    # 2~n 의 순열 구하기

    solve(0)
    print(f"#{tc} {minV}")
    