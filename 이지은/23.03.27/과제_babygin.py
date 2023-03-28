t = int(input())

def solve(arr):
    for i in set(arr):
        if arr.count(i) >= 3:
            return True

    tmp = 0
    tmp_arr = sorted(set(arr))
    for i in range(len(tmp_arr)-1):
        if tmp_arr[i] + 1 == tmp_arr[i+1]:
            tmp += 1
            if tmp >= 2:
                return True
        else:
            tmp = 0
    
    return False
    
for tc in range(1, t+1):
    player1 = []
    player2 = []
    
    num = list(map(int, list(input().split())))
    print(f"#{tc} ", end="")
    for i in range(0, 12, 2):

        player1.append(num[i])
        if len(player1) > 2 and solve(player1):
            print(1)
            break

        player2.append(num[i+1])
        if len(player2) > 2 and solve(player2):
            print(2)
            break
    else:
        print(0)
