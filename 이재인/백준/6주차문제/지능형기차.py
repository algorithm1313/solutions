train = [0]*4
for i in range(4):
    m, n = map(int, input().split())
    if i == 0 : 
        train[0] = n
    else:
        train[i] = train[i-1] + n-m

print(max(train))

    