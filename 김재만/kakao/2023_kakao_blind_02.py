# 택배 배달과 수거하기 lv2

## 1차 풀이 실패

def solution(cap, n, deliveries, pickups):
    answer = 0
    dist = n
    dist1 = dist2 = n
    
    while True:
        cover1 = cover2 = cap
        answer += dist*2
        flag = [0, 0]
        
        '''
        print("dist는", dist)
        print("del = ", deliveries, "현재 del 위치 = ", dist1)
        print("pic = ", pickups, "현재 pic 위치 = ", dist2)
        '''

        # 이게 한 싸이클
        for i in range(dist-1, -1, -1):
            if cover1 >= 0:
                del_cnt = deliveries[i]
                deliveries[i] = 0 if cover1 >= del_cnt else del_cnt - cover1
                cover1 -= del_cnt
                dist1 = i + 1
            else:
                flag[0] = 1

            if cover2 >= 0:
                pic_cnt = pickups[i]
                pickups[i] = 0 if cover2 >= pic_cnt else pic_cnt - cover2
                cover2 -= pic_cnt
                dist2 = i + 1
            else:
                flag[1] = 1
            
            if flag[0] == 1 and flag[1] == 1:
                break
        else:
            break

        dist = max(dist1, dist2)

    return answer
  
  
## 2차 풀이 성공

def solution(cap, n, deliveries, pickups):
    answer = 0
    give_bag = return_bag = 0
    
    for i in range(n-1, -1, -1):
        give_bag += deliveries[i]
        return_bag += pickups[i]
        
        while give_bag > 0 or return_bag > 0:
            give_bag -= cap
            return_bag -= cap
            answer += (i + 1) * 2

    return answer