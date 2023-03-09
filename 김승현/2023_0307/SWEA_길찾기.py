import sys
sys.stdin = open('길찾기.txt', 'r')

def dfs(s, v):
    visited = [0] * (v + 1)
    stack = []
    result = 0
    visited[s] = 1
    while True:
        if s == v:
            result = 1
            break

        for w in range(1, v + 1):
            if temp[s][w] == 1 and not visited[w]:
                stack.append(s)
                visited[w] = 1
                s = w
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break

    return result

for test_case in range(1, 11):
    T, E = map(int, input().split())
    num_list = list(map(int, input().split()))

    temp = [[0] * 100 for _ in range(100)]

    for i in range(0, E * 2, 2):
        start = num_list[i]
        end = num_list[i + 1]
        temp[start][end] = 1

    ans = dfs(0, 99)
    print(f'#{test_case} {ans}')

