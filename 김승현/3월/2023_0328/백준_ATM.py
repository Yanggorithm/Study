N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
temp = result = 0
for i in range(N):
    temp += num_list[i]
    result += temp

print(result)
