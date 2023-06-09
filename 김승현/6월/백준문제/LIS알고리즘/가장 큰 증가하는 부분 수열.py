import sys
input = sys.stdin.readline

N = int(input())

n_list = list(map(int, input().split()))

dp = [1] * N

# for i in range(N):


print(max(dp))