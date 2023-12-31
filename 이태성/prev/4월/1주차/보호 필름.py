def counting(film):
    for c in range(W):
        line = ""
        for r in range(D):
            line += film[r][c]
        if "1" * K in line or "0" * K in line:
            pass
        else:
            return False
    return True

def dfs(idx, selected):
    global min_cnt
    if min_cnt < len(selected):
        return

    if idx == D:
        if len(selected):
            one_or_zero(0, selected, [], [], film)
        return

    dfs(idx+1, selected+[idx])
    dfs(idx+1, selected)

def one_or_zero(idx, selected, A, B, film):
    global min_cnt

    if len(selected) > min_cnt:
        return

    if idx == len(selected):
        new_film = film[:]
        one = "1" * W
        zero = "0" * W
        # 바꾸기
        if A:
            for i in A:
                new_film[i] = one
        if B:
            for i in B:
                new_film[i] = zero

        if counting(new_film):
            if min_cnt > len(selected):
                min_cnt = len(selected)
        return

    one_or_zero(idx+1, selected, A+[selected[idx]], B, film)
    one_or_zero(idx+1, selected, A, B+[selected[idx]], film)

T = int(input())
for tc in range(1, T+1):
    # 두께, 가로, 합격기준
    D, W, K = map(int, input().split())
    film = []
    for _ in range(D):
        line = "".join(map(str, list(input().split())))
        film.append(line)
    min_cnt = K+1
    if counting(film):
        print(f"#{tc} {0}")
    else:
        dfs(0, [])
        print(f"#{tc} {min_cnt}")