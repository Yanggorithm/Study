import sys
from collections import deque

n = int(sys.stdin.readline().strip())
alphabet = dict()

for _ in range(n):
    a = sys.stdin.readline().strip()

    for i in range(len(a)):
        tmp = 10 ** (len(a) - i - 1)
        if not alphabet.get(a[i]):
            alphabet[a[i]] = 0
        alphabet[a[i]] += tmp

alphabet = sorted(list(alphabet.values()), reverse=True)
k = 9
ans = 0
for i in alphabet:
    ans += (i*k)
    k -= 1

print(ans) 
