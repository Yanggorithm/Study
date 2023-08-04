import sys
input = sys.stdin.readline

# 같은 무게 레일 x
# 레일 개수, 택배바구니 무게, 일의 시행횟수
n, m, k = map(int, input().strip().split())
lst = list(map(int, input().strip().split()))

mw = 2501

def rail_sum():
    global mw

    cw = 0
    index = 0
    tw = 0
    cnt = 0

    while cnt < k:
        if lst[index] + cw <= m:
            cw += lst[index]
        else:
            tw += cw
            cw = lst[index]
            cnt += 1
        index += 1
        if index == n:
            index -= n
    mw = min(mw, tw)   

def solve(i):
    global lst

    if i == n-1:
        rail_sum()
        return
    
    for j in range(i, n):
        lst[i], lst[j] = lst[j], lst[i]
        solve(i+1)
        lst[i], lst[j] = lst[j], lst[i]

solve(0)
print(mw)