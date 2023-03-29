import sys
input = sys.stdin.readline

N = int(input())
rope = [0] * N

for i in range(N):
    rope[i] = int(input())

rope.sort()
max_v = 0
for i in range(N):
    result = rope[i] * (N - i)
    max_v = max(max_v, result)

print(max_v)