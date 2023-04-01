h1 = "0F97A3"


def solution(n):
    ans = ""
    # n은 16진수 문자열
    for s in n:
        a = int(s, 16)
        for i in range(3, -1, -1):
            if a & (1 << i):
                ans += "1"
            else:
                ans += "0"

    return ans


print(solution(h1))


def solution2(n):
    l = len(n) * 4
    x = int(n, 16)
    result = ""

    for i in range(l - 1, -1, -7):
        bin = ""
        for j in range(7):
            if i - j < 0:
                break
            bin += "1" if x & (1 << i - j) else "0"
        print(bin, end=" ")
        dec = int(bin, 2)
        result += str(dec) + " "
    print()
    print(result)


solution2(h1)
