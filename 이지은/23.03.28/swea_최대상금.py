t = int(input())

def solve(c):
    global ans
    if c == chance:
        t = int(''.join(number))
        if ans < t:
            ans = t
        return

    for i in range(len(number)-1):
        for j in range(i+1, len(number)):
            number[i], number[j] = number[j], number[i]
            solve(c+1)
            number[i], number[j] = number[j], number[i]

for tc in range(1, t+1):    
    number, chance = input().split()
    number = list(number)
    chance = int(chance)

    ans = 0
    if chance > len(number):
        chance = len(number)

    if chance:
        solve(0)
        print(f"#{tc} {ans if ans else ''.join(number)}")
    else:
        print(f"#{tc} {''.join(number)}")
