# SWEA_1208 Flatten

def dump(cnt, boxes):
    while cnt:
        max_h, min_h = 1, 100
        max_i, min_i = 0, 0
        for i in range(100):
            if boxes[i] > max_h :
                max_h = boxes[i]
                max_i = i
            if boxes[i] < min_h :
                min_h = boxes[i]
                min_i = i
        boxes[max_i] -= 1
        boxes[min_i] += 1
        cnt -= 1
    
    return(max(boxes) - min(boxes))

T = 10
for TC in range(1,T+1):
    N = int(input())
    boxes = list(map(int,input().split()))

    print(f'#{TC}',dump(N,boxes))