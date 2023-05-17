n = int(input())

cnt = 99999999
for i in range(n//5+1):        
    if (n - 5*i) % 2 == 0:
        if cnt > i+(n-5*i)//2:
            cnt = i+(n-5*i)//2

if cnt == 99999999:
    print(-1)
else:
    print(cnt)