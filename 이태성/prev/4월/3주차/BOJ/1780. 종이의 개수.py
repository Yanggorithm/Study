import sys
input = sys.stdin.readline

def is_all_same(paper, x, y, size):
    # 해당 크기의 종이가 모두 같은 숫자로 이루어져 있는지 확인
    first = paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != first:
                return False
    return True

def divide_paper(paper, x, y, size, counts):
    # 해당 종이를 9개의 작은 종이로 나누어 숫자 개수 세기
    if is_all_same(paper, x, y, size):
        counts[paper[x][y]+1] += 1
    else:
        new_size = size // 3
        for i in range(3):
            for j in range(3):
                divide_paper(paper, x+i*new_size, y+j*new_size, new_size, counts)

def count_paper(paper, n):
    # -1, 0, 1로만 이루어진 종이의 개수 세기
    counts = [0, 0, 0]
    divide_paper(paper, 0, 0, n, counts)
    return counts

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
counts = count_paper(paper, n)
print(counts[0])
print(counts[1])
print(counts[2])
