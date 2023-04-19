N, S = map(int, input().split())
num_list = list(map(int, input().split()))
cnt = 0

def check(idx, total):
    global cnt
    if idx >= N:
        return

    total += num_list[idx]

    if total == S:
        cnt += 1

    check(idx + 1, total - num_list[idx])
    check(idx + 1, total)

check(0, 0)
print(cnt)