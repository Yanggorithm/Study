# 연습문제3
'''
0DEC
'''

pattern = ['001101',
           '010011',
           '111011',
           '110001',
           '100011',
           '110111',
           '001011',
           '111101',
           '011001',
           '101111']


def pw_solve(n):
    ans = ""
    result = ""
    for s in n:
        s = int(s, 16)
        for i in range(3,-1,-1):
            ans += "1" if s & (1<<i) else "0"

    print(ans)

    i = 0
    while i < len(ans)-6:
        if ans[i:i+6] in pattern:
            result += str(pattern.index(ans[i:i+6]))
            i += 6

        else:
            i += 1

    return result

n = input()
a = int(n,16)
print(a)
print(pw_solve(n))