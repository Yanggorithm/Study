t = int(input())

def mergeSort(m):
    # 종료
    if len(m) == 1:
        return m
    
    # 분할
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    # 정복
    left = mergeSort(left)
    right = mergeSort(right)

    # 병합
    return merge(left, right)

# 왼쪽과 오른쪽을 합쳐주는 함수
def merge(left, right):
    global cnt
    
    # 합병 하기 전에
    # left의 제일 끝, right의 제일 끝 비교
    if left[-1] > right[-1]:
        cnt += 1
    
    ln = len(left)
    rn = len(right)

    # 왼쪽에서 다음에 꺼낼 원소의 위치 : li
    # 오른쪽 : ri
    li = ri = 0
    
    # 결과 배열
    result = []
    # 왼쪽 또는 오른쪽에 원소가 하나라도 남아 있다면
    while li < ln or ri < rn:
        # 왼쪽 오른쪽 둘다 원소가 남아 있다면
        # 그중 작은 거부터 맨 앞에서 꺼내서 result에 추가
        if li < ln and ri < rn:
            if left[li] <= right[ri]:
                result.append(left[li])
                li += 1
            else:
                result.append(right[ri])
                ri += 1
        # 왼쪽만 남아 있으면 왼쪽거 추가
        elif li < ln:
            result.append(left[li])
            li += 1
        # 오른쪽만 남아 있으면 오른쪽 거 추가
        elif ri < rn:
            result.append(right[ri])
            ri += 1
        
        # 왼쪽 끝의 제일 끝 원소가 오른쪽 부분의 제일 끝 원소보다 클 경우
    return result


for tc in range(1, t+1):
    N= int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    mergeSort(arr)
    print(f"#{tc} {arr[N//2]} {cnt}")