N = int(input())
n_list = list(map(int, input().split()))

for i in range(1, N):
    n_list[i] = max(n_list[i], n_list[i] + n_list[i - 1])

print(max(n_list))