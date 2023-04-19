
change = input()
z_cnt = n_cnt = 0
prev = change[0]
if prev == '0':
    z_cnt += 1
else:
    n_cnt += 1

for i in range(1, len(change)):
    if prev == '1' and prev != change[i]:
        z_cnt += 1

    elif prev == '0' and prev != change[i]:
        n_cnt += 1

    prev = change[i]

if z_cnt == 0 or n_cnt == 0:
    print(0)
else:
    print(min(z_cnt, n_cnt))