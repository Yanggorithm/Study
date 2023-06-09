import sys

input = sys.stdin.readline

moeum = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
alpha = list(input().split())
alpha.sort()
# print(alpha)
visited = [0] * C
# print(visited)
result = set()


def check(cnt, start, temp, visit):
    if len(temp) == L:
        # print(temp)
        flag = 0
        count = 0
        for j in moeum:
            if j in temp:
                count += 1

        if count > 0 and L - count > 1:
            flag = 1

        if flag == 0:
            return

        temp2 = ""
        # temp.sort()
        for k in temp:
            temp2 += k

        result.add(temp2)
        return

    for i in range(start, C):
        if not visit[i]:
            visit[i] = 1
            temp.append(alpha[i])
            check(cnt + 1, i + 1, temp, visit)
            temp.pop()
            visit[i] = 0


check(0, 0, [], visited)

result = list(result)
result.sort()

for c in result:
    print(c)
