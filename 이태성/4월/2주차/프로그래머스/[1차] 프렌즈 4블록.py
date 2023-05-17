def solution(m, n, board):
    # 기존 배열을 리스트로 다시 저장
    new_board = []
    for line in board:
        new_board.append(list(line))

    answer = 0
    while True:
        change = set()
        tmp = ""
        for r in range(m - 1):
            for c in range(n - 1):
                ans = []
                tmp = new_board[r][c]
                # 4개가 같은지 확인하고
                if tmp:
                    for i in range(2):
                        for j in range(2):
                            ni = r + i
                            nj = c + j
                            if tmp == new_board[ni][nj]:
                                ans.append((ni, nj))
                    # 4개가 같으면 바꿔줘야 하는 위치를 set에 저장
                    if len(ans) == 4:
                        change = change | set(ans)
                else:
                    continue
        # 터뜨릴 값이 존재하면
        if change:
            # 터뜨릴 블록의 개수를 더해준다.
            answer += len(change)
            # 다 터뜨려서 빈 문자열을 반환
            for r, c in change:
                new_board[r][c] = ""

            # 재배치
            for c in range(n):
                idx = m - 1
                for r in range(m - 1, -1, -1):
                    if new_board[r][c]:
                        new_board[idx][c], new_board[r][c] = new_board[r][c], new_board[idx][c]
                        idx -= 1
        else:
            return answer

    return answer