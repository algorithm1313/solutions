# t = 상담하는데 걸리는 기간
# p = 상담하고 받을 수 있는 금액

def max_profit(N, schedule):
    # dp테이블 초기화
    dp = [0] * (N+1)

    # 거꾸로 비교 시작
    for i in range(N - 1, -1, -1):
        time = schedule[i][0]
        pay = schedule[i][1]
        
        if i + time <= N:
            dp[i] = max(pay+dp[i+time], dp[i+1])
        else:
            dp[i] = dp[i+1]
    return dp[0]

N = int(input())
schedule = []
for _ in range(N):
    t, p = map(int,input().split())
    schedule.append([t,p])

print(max_profit(N, schedule))
