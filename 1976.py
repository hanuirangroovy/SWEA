import sys
sys.stdin = open(f'input_1976.txt',"r")

def hour(h):
    if h>12:
        h -= 12
    return h

t = int(input())
for tc in range(1,t+1):
    h1, m1, h2, m2 = list(map(int, input().split()))

    h = h1+h2
    m = m1+m2

    if m > 60:
        result_m = m - 60
        h = h + 1

    else:
        result_m = m

    result_h = hour(h)
    print('#{} {} {}'.format(tc,result_h, result_m))