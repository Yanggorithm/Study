# 프로그래머스 PCCE 기출 9번 이웃한 칸

def solution(board, h, w):
    answer = 0
    N = len(board)
    color = board[h][w]
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = h + dr, w + dc
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == color:
            answer += 1
    return answer