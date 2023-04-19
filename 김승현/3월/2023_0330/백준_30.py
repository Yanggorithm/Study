
N = input()
total = 0
n_list = []
if '0' not in N:
    print(-1)
else:
    for i in range(len(N)):
        total += int(N[i])
        n_list.append(N[i])
    if total % 3 == 0:
        n_list.sort(reverse = True)
        t = int("".join(n_list))
        print(t)
    else:
        print(-1)