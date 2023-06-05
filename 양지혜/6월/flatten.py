import sys
sys.stdin = open('input(flatten).txt', "r")

T = 10
for tc in range(1, T+1):
    dump = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    # 정해진 횟수가 있으니까 while문 사용
    while dump > 0:
        # 리스트에 계산값을 적용해서 새로운 최대, 최솟값을 찾아야 함.
        # 인데스 함수를 사용하여 보았음
        temA = lst.index(max(lst))
        temB = lst.index(min(lst))

        lst[temA] -= 1
        lst[temB] += 1
        dump -= 1

        # 두 개의 차이점은 무엇인가 : 같은 최댓값이나 같은 최솟값이 있을 때
        # 덤프 후에 최대-최소 는 인덱스로 뽑은 그 값이 실제로는 최대, 최솟값이 아닐 수 있기 때문에
        # 특정하게 다시 그 바뀐 리스트에서 최댓값, 최솟값을 새로이 구해서 차이값을 구해야 한다!
        # ans = lst[temA] - lst[temB]
        ans = max(lst) - min(lst)

        if ans <= 1:
            break


    print(f"#{tc} {ans}")