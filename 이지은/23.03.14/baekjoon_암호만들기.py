import sys

l, c = map(int, sys.stdin.readline().strip().split())
arr = sys.stdin.readline().strip().split()
# 중복 없음.

# 최소 한개의 모음, 최소 두개의 자음
# 증가하는 순서로 배열
# 가능성 있는 암호들을 다 구한다.

vowel = []
for i in arr:
    if i in ['a','e','i','o','u']:
        vowel.append(i)

for i in vowel:
    if i in arr:
        arr.remove(i)

v = l-2

def solve_vowel(i, tmp):
    global result
    if len(tmp) == e:
        result.append(tmp.copy())
        return

    for j in range(i, len(vowel)):
        tmp.append(vowel[j])
        solve_vowel(j+1, tmp)
        tmp.pop()

def solve(i, tmp):
    global ans
    if len(tmp) == l:
        ans.append(sorted(tmp.copy()))
        return
    
    for j in range(i, len(arr)):
        tmp.append(arr[j])
        solve(j+1, tmp)
        tmp.pop()

result = []
ans = []
for e in range(1, v+1):
    solve_vowel(0, [])

for r in result:
    solve(0, r)

for a in sorted(ans):
    print("".join(a))