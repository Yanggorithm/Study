# SWEA_2112 보호 필름
# [출처] https://velog.io/@unani92 

def inspect(film,K):
    for i in range(W):
        stack = 0
        for j in range(D-1):
            if film[j][i] == film[j+1][i]:
                stack += 1
            else :
                stack = 0
            if stack == K-1 :
                break
        if stack != K-1 :
            return False
    return True

def dfs(L,s,film):
    global answer
    if L >= answer:
        return
    if inspect(film,K):
        if L < answer:
            answer = L
        return
    if L == K:
        if L < answer:
            answer = L
        return
    else :
        for i in range(s,D):
            switched = []
            for j in range(W):
                if film[i][j] == 1:
                    film[i][j] = 0
                    switched.append(j)
            dfs(L+1, i+1, film)
            for j in switched:
                film[i][j] = 1

            switched = []
            for j in range(W):
                if film[i][j] == 0:
                    film[i][j] = 1
                    switched.append(j)
            dfs(L+1, i+1, film)
            for j in switched:
                film[i][j] = 0

T = int(input())
for TC in range(1,1+T):

    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]
    answer = 1000000
    print(f'#{TC}', end=' ')
    if K == 1:
        print(0)
    else :
        dfs(0,0,films)
        print(answer)