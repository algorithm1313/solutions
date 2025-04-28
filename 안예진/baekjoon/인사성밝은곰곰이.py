n = int(input())  # 채팅 기록
result = 0
name = []

for _ in range(n):
    line = input()

    if line == "ENTER":
        name = []  
    elif line not in name:
        name.append(line)
        result += 1 

print(result)