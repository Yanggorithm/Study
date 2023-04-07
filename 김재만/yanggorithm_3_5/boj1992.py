# boj 1992 - 쿼드트리
# 4조각으로 나뉨 -> 재귀 4번 ? 이라고 생각이 됨
# N이 최대 64이므로 2^6 즉 최대 재귀 깊이 : 6 호출 은 최대 24번
# 충분히 재귀로 풀 수 있다.

# 풀이중

def recursion_tree(sx, ex, sy, ey):
    '''
    :param sx: 시작 x 인덱스
    :param ex: 끝 x 인덱스 + 1
    :param sy: 시작 y 인덱스
    :param ey: 끝 y 인덱스 + 1
    :return:
    '''
    check_set = set()

    for i in range(sx, ex):
        for j in range(sy, ey):
            check_set.add(q_tree[i][j])

    # 압축이 성공했다면
    if len(check_set) == 1:
        ans.append(list(check_set)[0])
        return
    # 압축이 실패 했으면?
    else:
        # print(ans)
        ans.append("(")
        # 4방향으로 쪼개기
        recursion_tree(sx, ((sx+ex) // 2), sy, ((sy+ey) // 2))
        recursion_tree(sx, ((sx+ex) // 2), ((sy+ey) // 2), ey)
        recursion_tree(((sx+ex) // 2), ex, sy, ((sy+ey) // 2))
        recursion_tree(((sx+ex) // 2), ex, ((sy+ey) // 2), ey)
        ans.append(")")


n = int(input())

q_tree = [list(input()) for _ in range(n)]
ans = []
recursion_tree(0, n, 0, n)

print("".join(ans))
