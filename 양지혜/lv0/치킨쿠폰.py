# 프로그래머스 Lv0 치킨쿠폰
def solution(chicken):
    service = 0
    # 초깃값 설정
    coupon = chicken
    while coupon >= 10:
        service += coupon // 10
        coupon = (coupon//10) + (coupon % 10)
        
    return service