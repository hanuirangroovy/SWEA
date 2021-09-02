import sys
sys.stdin = open(f'input_4299.txt',"r")

t = int(input())
for tc in range(1,t+1):
    d, h, m = list(map(int, input().split()))

    base = 11*24*60 + 11*60 + 11
    realized =  d*24*60 +h*60 + m
    result = realized - base
    if result<0:
        result = -1


    print('#{} {}'.format(tc,result))