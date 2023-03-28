import sys

# 49개의 수 중 k개를 골라 집합 S
# S 중에 6개 고르기

def solve(i, tmp):
    global result
    if len(tmp) == 6:
        result.append(tmp.copy())
        return
    
    for j in range(i, k):
        tmp.append(S[j])
        solve(j+1, tmp)
        tmp.pop()

while True:
    arr = sys.stdin.readline().strip()
    if len(arr) == 1:
        break
    else:
        k, *S = map(int, arr.split())
    
    result = []
    solve(0, [])
    for r in sorted(result):
        print(" ".join(map(str, r)))
    print()
