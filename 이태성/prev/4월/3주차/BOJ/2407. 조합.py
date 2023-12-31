n, m = map(int, input().split())
def recur(num):
    if num == 1:
        return 1
    return num * recur(num-1)
print(recur(n)//(recur(n-m)*recur(m)))
