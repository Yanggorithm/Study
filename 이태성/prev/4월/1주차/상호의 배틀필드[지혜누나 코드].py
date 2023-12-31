import sys

sys.stdin = open("input(상호샘플).txt", "r")

# 사방탐색(상하좌우)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


# 인덱스 유효성 검사
def is_valid(i, j):
    return 0 <= i < H and 0 <= j < W


# 사용자 입력 문자열 대로 움직이기
def command(si, sj):
    ci, cj = si, sj

    for comm in lst:
        if comm == 'U':
            # 전차가 바라보는 방향을 위로 바꾸고, 윗칸이 평지라면 이동
            # 윗칸이 평지인지 탐색
            ni = ci + di[0]
            nj = cj + dj[0]
            if is_valid(ni, nj) and arr[ni][nj] == '.':

                # 전치모양 맵에서 바꿔주기
                arr[ni][nj] = "^"
                arr[ci][cj] = "."
                ci, cj = ni, nj
            else:
                arr[ci][cj] = "^"


        elif comm == 'D':
            # 전차가 바라보는 방향을 아래로 바꾸고, 아랫칸이 평지라면 이동
            # 아랫칸이 평지인지 탐색
            ni = ci + di[1]
            nj = cj + dj[1]
            if is_valid(ni, nj) and arr[ni][nj] == '.':

                # 전치모양 맵에서 바꿔주기
                arr[ni][nj] = "v"
                arr[ci][cj] = "."
                ci, cj = ni, nj
            else:
                arr[ci][cj] = "v"

        elif comm == 'L':
            # 전차가 바라보는 방향을 왼쪽로 바꾸고, 왼쪽칸이 평지라면 이동
            # 왼쪽칸이 평지인지 탐색
            ni = ci + di[2]
            nj = cj + dj[2]
            if is_valid(ni, nj) and arr[ni][nj] == '.':

                # 전치모양 맵에서 바꿔주기
                arr[ni][nj] = "<"
                arr[ci][cj] = "."
                ci, cj = ni, nj
            else:
                arr[ci][cj] = "<"

        elif comm == 'R':
            # 전차가 바라보는 방향을 오른쪽으로 바꾸고, 오른쪽칸이 평지라면 이동
            # 오른쪽칸이 평지인지 탐색
            ni = ci + di[3]
            nj = cj + dj[3]
            if is_valid(ni, nj) and arr[ni][nj] == '.':

                # 전치모양 맵에서 바꿔주기
                arr[ni][nj] = ">"
                arr[ci][cj] = "."
                ci, cj = ni, nj
            else:
                arr[ci][cj] = ">"

        elif comm == 'S':
            # pass
            # 포탄발사
            # 게임맵 끝까지 "포탄이" 직진하기(전차가 보고있는 방향대로),
            # 벽돌로 만들어진 벽(*) 이면 평지(.)로 바뀐다, 포탄은 소멸(종료)
            # 강철로 만들어진 벽이면 아무일도 일어나지 않음
            # 물을 만났을 때 전차는 들어갈 수 없지만 포탄은 가능

            # 전차가 바라보고 있는 방향대로 구분하여 맵을 변경하도록 만들어보기
            # 상
            if arr[ci][cj] == "^":
                ni = ci + di[0]
                nj = cj + dj[0]
                for k in range(1, H):
                    if is_valid(ni, nj):
                        ni = ci + di[0] * k
                        nj = cj + dj[0] * k
                        if is_valid(ni, nj) and arr[ni][nj] == "*":
                            arr[ni][nj] = "."
                            pass

                        elif is_valid(ni, nj) and arr[ni][nj] == "#":
                            pass

                        else:
                            pass

                # 하
            elif arr[ci][cj] == "v":
                ni = ci + di[1]
                nj = cj + dj[1]
                if arr[ni][nj] == ".":
                    for k in range(1, H):
                        if is_valid(ni, nj) and arr[ni][nj]=='.':
                            ni = ci + di[1] * k
                            nj = cj + dj[1] * k

                if is_valid(ni, nj) and arr[ni][nj] == "*":
                    arr[ni][nj] = "."
                    pass

                elif is_valid(ni, nj) and arr[ni][nj] == "#":
                    pass
                else:
                    pass

                # 좌
            elif arr[ci][cj] == "<":
                ni = ci + di[2]
                nj = cj + dj[2]

                if arr[ni][nj] == ".":
                    for k in range(1, W):
                        if is_valid(ni, nj) and arr[ni][nj]=='.':
                            ni = ci + di[2] * k
                            nj = cj + dj[2] * k

                if is_valid(ni, nj) and arr[ni][nj] == "*":
                    arr[ni][nj] = "."
                    pass

                elif is_valid(ni, nj) and arr[ni][nj] == "#":
                    pass
                else:
                    pass
                # 우
            elif arr[ci][cj] == ">":
                ni = ci + di[3]
                nj = cj + dj[3]
                if arr[ni][nj] == ".":
                    for k in range(1, W):
                        if is_valid(ni, nj) and arr[ni][nj]=='.':
                            ni = ci + di[3] * k
                            nj = cj + dj[3] * k

                if is_valid(ni, nj) and arr[ni][nj] == "*":
                    arr[ni][nj] = "."
                    pass

                elif is_valid(ni, nj) and arr[ni][nj] == "#":
                    pass
                else:
                    pass
    return


T = int(input())
for tc in range(1, T + 1):
    # H: 맵의 높이, W : 너비
    H, W = map(int, input().split())
    # 게임맵
    arr = [list(input()) for _ in range(H)]

    # 사용자입력 갯수
    c = int(input())

    # 사용자 입력 문자
    lst = input()

    # 전차 위치 찾기(시작위치)
    si, sj = 0, 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == ">" or arr[i][j] == "<" or arr[i][j] == "v" or arr[i][j] == "^":
                si, sj = i, j
                break

    command(si, sj)

    print(f"#{tc}", end=" ")
    for mapp in arr:
        print("".join(mapp))