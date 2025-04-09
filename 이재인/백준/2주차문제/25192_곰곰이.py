import sys

n = int(input())  
li = []

for _ in range(n):
    li.append(sys.stdin.readline().strip())

check_set = set()  
answer = 0

for j in li:
    if j == "ENTER":
        check_set.clear()  
    else:
        if j not in check_set:  
            check_set.add(j)  
            answer += 1  

print(answer)
