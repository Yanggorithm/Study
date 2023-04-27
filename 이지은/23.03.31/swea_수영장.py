t = int(input())

def solve(n, sumV):
    if n > 12:
        ans = min(ans, sumV)
        return
    
    solve(n+1, sumV+day*plan[n])
    solve(n+1, sumV+mon)
    solve(n+3, sumV+mon3)
    solve(n+12, sumV+year)

for tc in range(1, t+1):
    day, mon, mon3, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    
    ans = 365*3000
    
