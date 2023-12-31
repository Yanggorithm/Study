import sys
input = sys.stdin.readline

# 해당 범위가 압축이 가능한지 찾는 함수
def check(sr, sc, N):
    tmp = video[sr][sc]
    for r in range(sr, sr+N):
        for c in range(sc, sc+N):
            # 가장 왼쪽 위 숫자를 기준으로 다른 숫자가 나오면
            # 압축이 불가능하다라는 의미
            if tmp != video[r][c]:
                return True
    # 압축이 가능하다는 의미
    return False

def Quad_Tree(sr, sc, N):
    tmp = video[sr][sc]

    if check(sr, sc, N):
        # 압축이 가능하지 않으면 여는 괄호를 프린트
        print("(", end="")
        N = N // 2
        Quad_Tree(sr, sc, N)        # 좌상
        Quad_Tree(sr, sc+N, N)      # 우상
        Quad_Tree(sr+N, sc, N)      # 좌하
        Quad_Tree(sr+N, sc+N, N)    # 우하
        print(")", end="")

    elif tmp == 1:
        print(1, end="")
    else:
        print(0, end="")

N = int(input())
video = [list(map(int, input().strip())) for _ in range(N)]
Quad_Tree(0, 0, N)