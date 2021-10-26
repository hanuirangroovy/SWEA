import sys
sys.stdin = open("input_2001.txt","r")


t = int(input())
for tc in range(1,t+1):
    n,m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for i in range(n-m+1):
        for j in range(n-m+1):
            sumV = 0
            for a in range(m):
                for b in range(m):
                    sumV += lst[i+a][j+b]
                    result.append(sumV)
    maxV = max(result)
    print('#{} {}'.format(tc,maxV))
