# 암호 만들기
import sys
input = sys.stdin.readline


# 순서가 잘 지켜지는 콤비네이션
def comb(cnt1, cnt2):
    
    if len(comb_list) == L:
        if cnt1 >= 1 and cnt2 >= 2:
            result.append(comb_list[:])
        return
    
    start = alphabets.index(comb_list[-1]) if comb_list else 0
    for i in range(start, C):
        if not visited[i]:
            visited[i] = 1
            comb_list.append(alphabets[i])
            if alphabets[i] in vowels:
                comb(cnt1+1, cnt2)
            else:
                comb(cnt1, cnt2+1)
            visited[i] = 0
            comb_list.pop()
        


vowels = ['a','e','i','o','u']
L, C = map(int,input().split())

alphabets = list(input().strip().split())
visited = [0] * C

alphabets.sort()

result = []
comb_list = []

comb(0, 0)
for ans in result:
    print("".join(ans))