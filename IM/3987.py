#위,오른쪽, 아래, 왼쪽
dx = [-1,0,1,0]
dy = [0,1,0,-1]
sig= ['U','R','D','L']

def signal(x,y):
    lst = []
    for dir in range(4):
        cnt = 1
        newx = x + dx[dir]
        newy = y + dy[dir]
        while 0 <= newx <n and 0<= newy < n and arr[newx][newy] != 'C':

            if arr[newx][newy] == '/':
                cnt += 1
                if dir == 0:
                    dir = 1
                elif dir == 1:
                    dir = 0
                elif dir == 2:
                    dir = 3
                elif dir == 3:
                    dir = 2
            if arr[newx][newy] == '\\':
                cnt += 1
                if dir == 0:
                    dir = 3
                elif dir == 1:
                    dir = 2
                elif dir == 2:
                    dir = 1
                elif dir == 3:
                    dir = 0
            cnt += 1
            newx += dx[dir]
            newy += dy[dir]
            if newx == x and newy == y and i==dir:
                print("Voyager")
                return
        lst.append(cnt)

    print(lst)
    #print(max(lst))


n, m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
pr, pc = map(int,input().split())
x = pr - 1
y = pc - 1
signal(x,y)
