a = input()

ans = ""


for s in a:
    b = int(s, 16)
    for j in range(3,-1,-1):
        ans += "1" if b & (1<<j) else "0"

print(int(a,16))
print(ans)