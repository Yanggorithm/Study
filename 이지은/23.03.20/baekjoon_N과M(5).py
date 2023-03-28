import sys

def nm(i):
    global result
    # 1. 종료조건
    if i == n:
        temp = ""
        for k in range(0, m):
            temp += f"{numbers[k]} "
        result.append(temp)
    
    # 2.재귀호출
    # 현재 위치 i에서 다른 위치 j에 있는 숫자와 한번씩 다 바꿔보기
    for j in range(i, n):
        numbers[i], numbers[j] = numbers[j], numbers[i]
        nm(i+1)
        numbers[i], numbers[j] = numbers[j], numbers[i]
        
n, m = map(int, sys.stdin.readline().strip().split())
numbers = sorted(list(map(int, sys.stdin.readline().strip().split())))
result = []

nm(0)
ans = []
for i in list(set(result)):
    ans.append(list(map(int, i.split())))

for i in sorted(ans):
    print(' '.join(map(str, i)))