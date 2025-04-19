# n, k = map(int, input().split())

# hour = 0
# min = 0
# sec = 0
# count=0
# while hour <= n:
#     if str(k) in str(sec) or str(k) in str(min) or str(k) in str(hour):
#         count +=1 
#     sec+=1
#     if sec == 60 :
#         sec = 0
#         min += 1
        
#     if min == 60 :
#         min =0
#         hour += 1
        
# print(count)

n, k = map(int, input().split())
count = 0
for hour in range(n+1):
    for minute in range(60):
        for sec in range(60):
            if str(k) in f"{hour}{minute}{sec}":
                count+=1
print(count)
