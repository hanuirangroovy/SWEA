import sys
sys.stdin = open("input_1859.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    case = list(map(int, input().split()))
    start = 0
    result = 0
    while start < n:
        sell = 0
        day = 0
        # 파는 지점 찾기
        for i in range(start,n):
            if case[i] > sell:
                sell = case[i]
                day = i
        # 시작점부터 파는 지점까지 가격 구하기
        for j in range(start, day):
            result += sell - case[j]
        start = day + 1 #시작점 재설정
    print('#{} {}'.format(tc, result))




