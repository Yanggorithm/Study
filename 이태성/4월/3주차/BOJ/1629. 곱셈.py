A, B, C = map(int, input().split())
def Divide_And_Conquer(A, B):
    if B == 1:
        return A % C
    else:
        tmp = Divide_And_Conquer(A, B//2)
        if B % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * A) % C
print(Divide_And_Conquer(A, B))