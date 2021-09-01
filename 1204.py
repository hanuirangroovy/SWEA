import sys
sys.stdin = open("input_1204.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    case = list(map(int, input().split()))
    cnt_max = 0
    #cnt 만들어서 나온 수만큼 해당 칸에 집어넣기
    cnt = [0] * 101
    for i in range(len(case)):
        cnt[case[i]] += 1
        max_cnt = max(cnt)
    for j in range(100):
        if cnt[j] == max_cnt:
            result = j
    # for j in range(1,101):
    #     if cnt[j] >= cnt_max:
    #         cnt_max = cnt[j]
    #         result = j
    print('#{} {}'.format(tc, result))
