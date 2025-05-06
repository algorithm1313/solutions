import sys

train = []
current = 0
for i in range(4):
    out, on = map(int, sys.stdin.readline().strip().split())
    if len(train) == 0:
        train.append(on)
        current = on
    else:
        current = current + on - out
        train.append(current)
print(max(train))
