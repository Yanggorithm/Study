import sys
input = sys.stdin.readline

def check(idx, value):

    for i in range(idx + 1, N):
        if value > num_list[i]:
            num_list[idx], num_list[i] = num_list[i], num_list[idx]
            idx = i
        else:
            return

N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))

num_list.sort()

total = 0
for i in range(1, N):
    num_list[i] = num_list[i] + num_list[i - 1]
    total += num_list[i]
    check(i, num_list[i])

print(total)