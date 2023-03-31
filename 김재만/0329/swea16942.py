# 실습 53
# 퀵솔트

def quick_sort(l, r):
    pivot = A[l]
    i = l
    j = r

    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]
    return j


def quick(l, r):

    if l < r:
        p = quick_sort(l, r)
        quick(l, p - 1)
        quick(p + 1, r)


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    A = list(map(int, input().split()))

    quick(0, n - 1)
    print(f"#{tc} {A[n//2]}")
