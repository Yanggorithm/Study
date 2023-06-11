park=["OSO","OOO","OXO","OOO"]
routes=["E 2","S 3","W 1"]
def solution(park, routes):
    move={"N":(-1,0),"S":(1,0),"W":(0,-1),"E":(0,1)}
    forbiddeni=len(park) #가면 안되는 구역 제한
    forbiddenj=len(park[0]) #가면 안되는 구역 제한

    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=="S":
                si=i #시작점i
                sj=j #시작점j

    for route in routes:
        dr,dc=move[route[0]]
        reali=si
        realj=sj
        for x in range(int(route[2])):
            if 0<=reali+dr<forbiddeni and 0<=realj+dc<forbiddenj and park[reali+dr][realj+dc]!="X":
                reali= reali+dr #통과되면 real로 바꿔준다!
                realj= realj+dc
            else: #통과 안되면 그 전으로 돌려놔!
                reali=si
                realj=sj
                break 
                #안쓰면 이미 장애물만났거나 조건에 해당안되어서 버려야하는데 다시 돌아가서 안버려짐
        si=reali 
        #안하면 자꾸 for문으로 돌아가서 reali와 realj가 0으로 초기화됨
        sj=realj 
        #si값이 reali가 되니까 si값도 바꿔주어야 for문 돌릴때 정상으로 돌아간다
    return ([reali,realj])