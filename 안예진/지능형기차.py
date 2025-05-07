max = 0  # 지금까지 가장 많았던 사람 수
current = 0     # 현재 기차 안 사람 수

for i in range(4):
    outpeople, inpeople = map(int, input().split())  # 내린 사람과 탄 사람 입력
    current -= outpeople  # 내리고 -> 
    current += inpeople   # 그다음 탐
    if current > max:  # 최대값
        max = current

print(max)