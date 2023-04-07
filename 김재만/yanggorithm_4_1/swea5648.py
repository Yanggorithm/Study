# 원자 소멸 시뮬레이션

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    result = 0
    star_box = []

    # star_box [x,y]:0, d:1, k:2
    for _ in range(n):
        x, y, d, k = map(int, input().split())
        # 중간에서 만나 지나치는경우를 방지하기 위해 배치 칸을 2배 늘려줌
        x, y = x*2, y*2
        star_box.append([[x, y], d, k])

    # maximum 4002번째 까지 돌 수 있다.
    for _ in range(4002):
        fire = set()
        # star_box 가 비어있으면 돌지마라 즉 다 터졌으면,
        if star_box:
            # 다들 한칸씩 움직여
            for i in range(len(star_box)):
                # x, y 값 변화
                star_box[i][0][0] += dx[star_box[i][1]]
                star_box[i][0][1] += dy[star_box[i][1]]
                fire.add(tuple(star_box[i][0]))
            # 다 한칸씩 움직였다면 -> 폭발이 일어 났나보자
            else:
                # 폭발이 일어났다면?
                if len(fire) != len(star_box):
                    # 폭발 일어난 곳 찾기.
                    for find_num in list(fire):
                        kk = 0
                        idx_list = []
                        # star_list = [[x,y], d, k]
                        for idx, star_list in enumerate(star_box):
                            if star_list[0] == list(find_num):
                                kk += star_list[2]
                                idx_list.append(idx)

                        # 폭발이 일어난곳.
                        if len(idx_list) > 1:
                            result += kk
                            p_index = 0
                            for pp in idx_list:
                                pp -= p_index
                                star_box.pop(pp)
                                p_index += 1

        else:
            break

    print(f"#{tc} {result}")