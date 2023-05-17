import sys
input = sys.stdin.readline
N, K = map(int, input().split())
antatica = ["a", "n", "t", "i", "c"]
Etc = set()
words = []
ans = maxCnt = 0
for _ in range(N):
    string = input().strip()[4:-4]
    if string:
        tmp = set(string)
        words.append(tmp)
        for i in tmp:
            if i not in antatica:
                Etc.add(i)
    else:
        maxCnt += 1
Etc = list(Etc)

def dfs(depth, length, selected):
    global maxCnt
    # 가지 치기
    #
    if depth == len(Etc):
        cnt = 0
        if length == (K-5):
            for word in words:
                possible = True
                for alpha in word:
                    if alpha not in selected+antatica:
                        possible = False
                        break
                if possible:
                    cnt += 1
            maxCnt = max(maxCnt, cnt)
        return
    dfs(depth+1, length+1, selected+[Etc[depth]])
    dfs(depth+1, length, selected)

if K < 5:
    print(0)
else:
    dfs(0, 0, [])
    print(maxCnt)