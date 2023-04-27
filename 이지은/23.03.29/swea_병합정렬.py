def merge_sort(left, right):
    global ans

    if left == right-1:
        return
    
    # 분할
    mid = (left + right) // 2
    if tmp[mid-1] > tmp[right-1]:
        ans += 1

    merge_sort(left, mid)
    merge_sort(mid, right)

    # 결합
    l, r = left, mid
    if arr[mid-1] > arr[right-1]:
        ans += 1
    
    for k in range(left, right):
        if r >= right:
            tmp[k] = arr[l]
            l += 1
        elif l >= mid:
            tmp[k] = arr[r]
            r += 1
        elif arr[l] <= arr[r]:
            tmp[k] = arr[l]
            l += 1
        else:
            tmp[k] = arr[r]
            r += 1
    
    for i in range(left, right):
        arr[i] = tmp[i]
        
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * n

    # n//2번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수
    ans = 0

    merge_sort(0, n)
    print(f"#{tc} {arr[n//2]} {ans}")
    
    