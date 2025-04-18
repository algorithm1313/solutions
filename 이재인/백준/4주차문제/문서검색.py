import sys
input = sys.stdin.readline

doc = list(input().strip())
a = list(input().strip())


count =0
i=0
while i<len(doc):
    if doc[i:i+len(a)] == a:
        i += len(a)
        count += 1
    else: i+=1
print(count)