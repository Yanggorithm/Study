import sys
input = sys.stdin.readline

def get_result(lst):
    result = 0
    for k in range(len(lst)-1):
        result += abs(lst[k] - lst[k+1])
    return result

def perm(i):
    global maxV
    if i == n:
        tmp = get_result(num)
        if tmp > maxV:
            maxV = tmp
        return
    
    for j in range(i, n):
        num[i], num[j] = num[j], num[i]
        perm(i+1)
        num[i], num[j] = num[j], num[i]
        
n = int(input().strip())
num = list(map(int, input().strip().split()))
maxV = 0
perm(0)
print(maxV)