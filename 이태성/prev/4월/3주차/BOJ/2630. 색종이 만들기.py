import sys
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def is_all_same(r, c, size):
    first = paper[r][c]
    for p in range(r, r+size):
        for q in range(c, c+size):
            if paper[p][q] != first:
                return False
    return True

def divide_paper(r, c, size, counts):
    if is_all_same(r, c, size):
        counts[paper[r][c]] += 1
    else:
        new_size = size // 2
        for p in range(2):
            for q in range(2):
                divide_paper(r+p*new_size, c+q*new_size, new_size, counts)

def count_paper(N):
    counts = [0, 0]
    divide_paper(0, 0, N, counts)
    return counts

counts = count_paper(N)
print(counts[0])
print(counts[1])