import sys

n = int(sys.stdin.readline().strip())

persons = set()
count = 0
for i in range(n):
    person = sys.stdin.readline().strip()
    
    if person == 'ENTER':
        persons = set()
    else:
        if person not in persons:
            count += 1
            persons.add(person)

print(count)
