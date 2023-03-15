import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
L, C = map(int, input().split())
Alphabet = sorted(list(map(str, input().split())))
vowels = ["a", "i", "u", "e", "o"]
password = []
def check(stack):
    vo = co = 0
    for alp in stack:
        if alp in vowels:
            vo += 1
        else:
            co += 1
    return vo >= 1 and co >= 2

def back(start, depth):
    if depth == L and check(password):
        print("".join(map(str, password)))
        return
    for idx in range(start, C):
        password.append(Alphabet[idx])
        back(idx+1, depth+1)
        password.pop()
back(0, 0)