import sys
input = sys.stdin.readline
N, K = map(int, input().split())
antatica = ["a", "n", "t", "i", "c"]
Etc = set()
words = []
ans = 0
for _ in range(N):
    string = input().strip()[4:-4]
    tmp = list(set(string))
    for i in string:
        if tmp and i in antatica:
            tmp.remove(i)
    words.append(tmp)

    Etc = Etc.union(tmp)
Etc = list(Etc)
maxCnt = 0
results = []
def dfs(depth, selected):
    global maxCnt
    if depth == len(Etc):
        selected = set(selected)
        if len(selected) == (K-5):
            results.append(selected)
        return
    dfs(depth+1, selected+[Etc[depth]])
    dfs(depth+1, selected)

if K < 5:
    print(0)
else:
    dfs(0, [])
    for result in results:
        cnt = 0
        for word in words:
            ans = True
            for alpha in word:
                if alpha not in result:
                    ans = False
                    break
            if ans:
                cnt += 1
        if maxCnt < cnt:
            maxCnt = cnt
    print(maxCnt)