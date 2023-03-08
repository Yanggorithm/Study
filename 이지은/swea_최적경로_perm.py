# 메모리초과
def perm(i):
    global result
    if i == n:
        result.append(customer.copy())
        return
    
    for j in range(i, n):
        customer[i], customer[j] = customer[j], customer[i]
        perm(i+1)
        customer[i], customer[j] = customer[j], customer[i]

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    wi, wj, hi, hj, *arr = map(int, input().split())

    customer = []
    for i in range(0, n*2, 2):
        customer.append(tuple(arr[i: i+2]))

    result = []
    perm(0)
    minV = 100000
    for r in result:
        tmp = abs(wi-r[0][0]) + abs(wj-r[0][1]) + abs(hi-r[n-1][0]) + abs(hj-r[n-1][1])
        for i in range(n-1):
            tmp += (abs(r[i][0]-r[i+1][0]) + abs(r[i][1]-r[i+1][1]))
        if tmp < minV:
            minV = tmp
    
    print(f"#{tc} {minV}")
            
    
    