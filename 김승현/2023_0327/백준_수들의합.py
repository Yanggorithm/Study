N = int(input())

total = 0
n = 1
while True:
    if total >= N:
        print(n - 1)
        break

    n += 1
    total += n


