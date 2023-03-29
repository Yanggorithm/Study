def dfs(start, end):
    stack = []
    visit[start] = 1

    while True:
        for c in adj[start]:
            if visit[c] == 0:
                stack.append(start)
                start = c
                visit[start] = 1
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break
    return

t = 10
for tc in range(1, t+1):
    # e: 길(간선) 총 개수
    _, e = map(int, input().split())
    road = list(map(int, input().split()))
    v = 100    # 정점 개수 최대 100개
    start, end = 0, 99
    adj = [[] for _ in range(100)]
    for i in range(0, len(road), 2):
        c1, c2 = road[i], road[i+1]
        # 인접 배열에 연결 저장
        adj[c1].append(c2)

    visit = [0] * 100
    dfs(start, end)
    print(f'#{tc} {visit[end]}')

'''
1. list 로 연결 정보 받기
2. 2개씩 끊어서 인접 배열에 저장
3. 방문 배열 만들기
4. bfs 함수 생성
    stack 만들고 출발점 방문기록
    while 문 start 를 인덱스로 인접배열 탐색
    c에 방문하지 않았다면 스택에 start 넣고 start 를 c로 바꾸기
    start 방문 기록하고 중단
    인접 배열에 없는 경우, 스택에 값이 있다면, 스택에서 꺼내서 start 에 저장
    스택에 값이 없다면 중단
'''
