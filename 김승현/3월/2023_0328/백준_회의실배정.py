from sys import stdin

N = int(stdin.readline())

room = []
for i in range(N):
    room.append(list(map(int, stdin.readline().split())))

room.sort(key = lambda x : (x[1],x[0]))

room_s = room[0][1]
cnt = 1

for i in range(1, N):
    if room_s <= room[i][0]:
        cnt += 1
        room_s = room[i][1]

print(cnt)
