t = int(input())

def solve(i, cnt, battery):
    global result

    if cnt >= result:
        return
    
    # 종료조건
    if i == n-2:
        result = min(cnt, result)
        return
    

    for j in range(1, battery+1):
        if i+j > n-2:
            result = min(cnt, result)
            return

        solve(i+j, cnt+1, arr[i+j])       

for tc in range(1, t+1):
    n, *arr = map(int, input().split())
    arr += [0]

    result = n-1

    solve(0, 0, arr[0])
    print(f"#{tc} {result}")