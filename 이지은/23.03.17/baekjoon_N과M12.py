def backtracking():
    global result

    # 1. 종료조건
    if len(s) == m:
        result.append(' '.join(map(str, s)))
        return
                
    # 2. 재귀호출
    for i in range(len(arr)):
        s.append(arr[i])
        backtracking()
        s.pop()
    
import sys
n, m = map(int, sys.stdin.readline().strip().split())
arr = sorted(set(map(int, sys.stdin.readline().strip().split())))
result = []
selected = [0] * len(arr)
s = []
backtracking()
print("\n".join(sorted(result)))
