import sys
sys.stdin = open("input_11671.txt","r")

# 좌, 우, 상, 하
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def change(x,y,k):
    for a in range(4):
        for b in range(1,k+1):
            newx = x + dx[a]*b
            newy = y + dy[a]*b
            #공간 벗어나는 경우 무시
            if newx < 0 or newx >= n or newy <0 or newy >= n:
                continue
            if arr[newx][newy] == 'H':
                arr[newx][newy] = 'X'

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':
                change(i, j, 1)
            elif arr[i][j] == 'B':
                change(i, j, 2)
            elif arr[i][j] == 'C':
                change(i, j, 3)
            if arr[i][j] == 'H':
                 cnt += 1
    # for lst in arr:
    #     cnt += lst.count('H')
    print('#{} {}'.format(tc, cnt))


def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 인덱스체크, H일때 X로 바꾸기
        for j in range(ord(arr[x][y])-ord('A') + 1):
            if 0 <= nx < N and 0 <= ny < N :
                if arr[nx][ny] == 'H':
                    arr[nx][ny] = 'X'
                nx = nx + dx[i]
                ny = ny + dy[i]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#
#     # 기지국 찾기
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C':
#                 check(i, j)
#     # 4방향 돌려서 커버되는 H -> X
#     # H 세기
#     ans = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 'H':
#                 ans += 1
#
#     print("#{} {}".format(tc, ans))
#     for i in arr:
#         print(*i)