T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    atom = [list(map(int, input().split())) for _ in range(n)]
    # 격자 중간에서 만날 수도 있기 때문에 0.5초 단위로 이동한다고 가정했음
    d = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]

    result = 0

    # 아톰 개수가 2개 이하가 되면 만날 아톰이 없으니까 종료
    while len(atom) >= 2:
        # 모든 아톰을 0.5초 단위로 이동시킨다
        for i in range(len(atom)):
            atom[i][0] = atom[i][0] + d[atom[i][2]][0]
            atom[i][1] = atom[i][1] + d[atom[i][2]][1]

        # 좌표를 딕셔너리로 표현
        location = {}
        # 각 아톰들을 순회하면서 좌표: [아톰들]의 형태로 넣어준다.
        for a in atom:
            try:
                location[(a[0], a[1])].append(a)
            except Exception:
                location[(a[0], a[1])] = [a]

        # 아톰 리스트를 초기화하고
        atom = []
        for l in location:

            if len(location[l]) >= 2:
                # 만약 같은 위치에 아톰이 여러개라면 결과값에 아톰의 에너지들을 결과값에 넣어주고
                for at in location[l]:
                    result += at[3]
            else:
                # 위치에 아톰이 1개라면 범위내에 있는 아톰들은 아톰 리스트에 다시 넣어준다.
                if -1000 <= location[l][0][0] <= 1000 and -1000 <= location[l][0][1] <= 1000:
                    atom.append(location[l][0])

    print(f'#{tc}', result)