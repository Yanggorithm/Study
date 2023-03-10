# 노드의 거리
# 방향 없는 간선 / 최소 몇개의 간선을 지나야 도착할 수 있는지?

'''
bfs 함수
1. 방문 리스트 생성 [0] * (노드 개수+1)
2. q 만들고 시작점 넣기
3. 시작점 방문 기록하기 (1)
4. q 에 값이 있는 동안 반복
    1) q 에서 위치 하나 꺼내서 t 에 저장
    2) 그래프 t 위치 값이 방문한 자리가 아니라면
        q 에 그 자리(nt) 넣고, 방문 기록 (1)
    3) 그 자리가 목표 지점이 아니라면 ?????? 방문     
'''
# 그래프 정보/시작/도착/노드
def bfs(graph, start, goal, v):
    visit = [0] * (v+1)
    q = [start]
    # q = []
    # q.append(start)
    visit[start] = 1

    while q:
        t = q.pop(0)
        # 그래프의 t번째 인덱스 번호와 연결된 노드 반복 비교
        for nt in graph[t]:
            # 연결 노드가 방문한 곳이 아니라면 그 노드를 q에 넣고 방문 기록하기
            if not visit[nt]:
                q.append(nt)
                # 그래프 인덱스와 맞춰주기 위해 +1
                visit[nt] = visit[t] + 1

                # 해당 노드가 목표 지점이라면 +1 해준거 빼기
                if nt == goal:
                    return visit[nt] - 1


    # 목표 지점 만나지 못했다면 0 반환
    return 0

t = int(input())
for tc in range(1, t+1):
    # v: 노드 개수, e: 간선 개수
    v, e = map(int, input().split())
    # 인덱스 세기 편하게 +1 크기로 그래프 만들기
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        # 간선 개수 e에 따른 양쪽 노드 번호
        n1, n2 = map(int, input().split())
        # 그래프에 연결 정보 저장
        graph[n1].append(n2)
        graph[n2].append(n1)

    # start: 출발 노드, goal: 도착 노드
    start, goal = map(int, input().split())

    print(f'#{tc} {bfs(graph, start, goal, v)}')
