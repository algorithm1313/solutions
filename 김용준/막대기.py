import sys

n = int(sys.stdin.readline().strip()) 

sticks = []
for i in range(n):
    sticks.append(int(sys.stdin.readline().strip()))
sticks = sticks[::-1]  

count = 1  
max_height = sticks[0] 
for i in range(1, n):
    if sticks[i] > max_height:  
        count += 1
        max_height = sticks[i]

print(count)
