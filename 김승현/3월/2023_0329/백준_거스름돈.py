N = int(input())

cnt = 0

res = int(N / 5)
t = N % 5
cnt += res
if N > 5:
    if t == 4:
        cnt += 2
    elif t == 3:
        cnt += 3
    elif t == 2:
        cnt += 1
    elif t == 1:
        cnt += 2
else:
    if N == 5:
        cnt = 1
    elif N == 4:
        cnt = 2
    elif N == 3 or N == 1:
        cnt = -1
    elif N == 2:
        cnt = 1

print(cnt)