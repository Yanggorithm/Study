# 로또

def comb(k):
    
    if len(comb_list) == 6:
        print(" ".join(list(map(str,comb_list))))
        return
    
    start = s.index(comb_list[-1]) if comb_list else 0
    for i in range(start,k):
        if not visited[i]:
            visited[i] = 1
            comb_list.append(s[i])
            comb(k)
            comb_list.pop()
            visited[i] = 0


while True:
    k, *s = map(int,input().split())
    comb_list = []
    visited = [0] * k
    
    if k == 0:
        break
    else:
        comb(k)
        print()

