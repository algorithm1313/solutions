
import sys

n = int(input())
height = [int(sys.stdin.readline()) for _ in range(n)]

max_height = 0
visible_count = 0

for h in reversed(height):
    if h > max_height:
        max_height = h
        visible_count += 1

print(visible_count)