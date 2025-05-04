max_people = 0
curr = 0
for i in range(4):
    a, b = map(int, input().split())
    curr = curr + b - a
    max_people = max(curr, max_people)
print(max_people)
