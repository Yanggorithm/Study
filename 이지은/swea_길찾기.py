for tc in range(1, 11):
    t, n = map(int, input().split())
    arr = list(map(int, input().split()))

    node = [[] for _ in range(100)]
    visited = [0] * 100
    
    for i in range(0, n*2, 2):
        node[arr[i]].append(arr[i+1])
    
    stack = [0]

    def solve():
        while stack:
            ni = stack.pop()
            for i in node[ni]:
                stack.append(i)
                visited[i] = 1
            if visited[99] == 1:
                return 1
        return 0
    
    print(f"#{tc} {solve()}")
