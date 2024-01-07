from collections import deque


def solution(places):
    answer = []
    # 5 * 5
    # 거리 2 이하는 안돼
    # P 응시자
    # O는 빈 테이블
    # X는 파티션
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def isValid(nr, nc):
        return 0 <= nr < 5 and 0 <= nc < 5

    for place in places:
        isNotValid = False
        for sr in range(5):
            for sc in range(5):
                if place[sr][sc] == "P":
                    V = [[-1 for _ in range(5)] for _ in range(5)]
                    V[sr][sc] = 0
                    q = deque([(sr, sc)])
                    while q:
                        r, c = q.popleft()
                        for d in range(4):
                            nr = r + dr[d]
                            nc = c + dc[d]
                            if (
                                isValid(nr, nc)
                                and place[nr][nc] != "X"
                                and V[nr][nc] == -1
                            ):
                                V[nr][nc] = V[r][c] + 1
                                if place[nr][nc] == "P":
                                    if V[nr][nc] < 3:
                                        isNotValid = True
                                        answer.append(0)
                                        break
                                else:
                                    q.append((nr, nc))
                        if isNotValid:
                            break
                if isNotValid:
                    break
            if isNotValid:
                break
        if isNotValid == False:
            answer.append(1)
    return answer
