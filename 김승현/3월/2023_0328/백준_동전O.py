
N, K = map(int, input().split())
coin = []
cnt = 0
for i in range(N):
    coin.append(int(input()))

coin.sort(reverse = True)

for i in range(N):
    t = K // coin[i]
    if t != 0:
        cnt += t
        K -= t * coin[i]

print(cnt)
