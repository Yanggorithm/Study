t = int(input())


def binarySearch(A, N, key):
    low, high = 0, N-1
    flag = 0

    while low <= high:
        mid = (low+high)//2
        
        if A[mid] == key:
                return 1
        elif A[mid] > key and flag >=0:
            high = mid - 1
            flag = -1
        elif A[mid] < key and flag <= 0:
            low = mid + 1
            flag = 1
        else:
            return 0

    return 0


for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr_n = sorted(list(map(int, input().split())))
    arr_m = sorted(list(map(int, input().split())))

    result = 0
    for i in arr_m:
        result += binarySearch(arr_n, n, i)

    print(f"#{tc} {result}")
