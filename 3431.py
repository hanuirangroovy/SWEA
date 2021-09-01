import sys
sys.stdin = open("input_3431.txt", "r")

t = int(input())
for tc in range(1,t+1):
    l, u, x = map(int, input().split())
    if l <= x <= u:
        result = 0
    if x > u:
        result = -1
    if x < l:
        result = l-x
    print('#{} {}'.format(tc, result))
