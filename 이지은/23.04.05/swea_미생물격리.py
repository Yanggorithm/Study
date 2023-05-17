t = int(input())
di, dj = [0,-1,1,0,0], [0,0,0,-1,1]
tbl = [0,2,1,4,3]
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(k)]

    for _ in range(m):
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + di[arr[i][3]]
            arr[i][1] = arr[i][1] + dj[arr[i][3]]
            if arr[i][0] == 0 or arr[i][0] == n-1 or arr[i][1] == 0 or arr[i][1] == n-1:
                arr[i][2] //= 2
                arr[i][3] = tbl[arr[i][3]]
        
        arr.sort(key=lambda x:(x[0], x[1], x[2]), reverse=True)

        i=1
        while i < len(arr):
            if arr[i-1][0:2] == arr[i][0:2]:
                arr[i-1][2] += arr[i][2]
                arr.pop(i)
            else:
                i+=1
                
            
