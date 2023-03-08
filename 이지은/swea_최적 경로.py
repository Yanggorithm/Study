# 오답
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    wi, wj, hi, hj, *arr = map(int, input().split())

    customer = []
    for i in range(0, n*2, 2):
        customer.append(tuple(arr[i: i+2]))

    stack = [(wi, wj)]
    way = 0
    while stack:
        minV = 200
        mi = 0
        ci, cj = stack.pop()
        if customer:
            for i in range(len(customer)):
                tmp = abs(ci-customer[i][0]) + abs(cj-customer[i][1])
                if minV > tmp:
                    minV = tmp
                    mi = i
            way += minV
            stack.append((customer[mi][0], customer[mi][1]))
            customer.remove((customer[mi][0], customer[mi][1]))
        else:
            way += (abs(ci - hi) + abs(cj - hj))

    print(f"#{tc} {way}")
            
    
    