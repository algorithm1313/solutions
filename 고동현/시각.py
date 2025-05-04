n, k = map(int,input().split())
k = str(k)

hour_in_k = 0
for h in range(n+1):
    if k in str(h):
        hour_in_k += 1

minute_in_k = 0
for m in range(60):
    if k in str(m):
        minute_in_k += 1

sec_in_k = 0
for s in range(60):
    if k in str(s):
        sec_in_k += 1

answer = hour_in_k * 3600 + (minute_in_k * 60 * (n+1 - hour_in_k)) + (sec_in_k * (60-minute_in_k) * (n+1-hour_in_k))
print(answer)