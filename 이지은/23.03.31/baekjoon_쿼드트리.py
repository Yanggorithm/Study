import sys

n = int(sys.stdin.readline().strip())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

ans = ""
def solve(si, sj, w):
    global ans
    check = set()
    flag = 0
    for i in range(si, si+w):
        for j in range(sj, sj + w):
            check.add(arr[i][j])

            if len(check) == 2:
                flag = 1
                break
        if flag:
            break
    
    if flag:
        ans += "("
        solve(si, sj, w//2)
        solve(si, sj+w//2, w//2)
        solve(si+w//2, sj, w//2)
        solve(si+w//2, sj+w//2, w//2)
        ans += ")"
    else:
        check = list(check)
        ans += check[0]


solve(0, 0, n)
print(ans)