import sys

strs = sys.stdin.readline().rstrip('\n')

answer = ''
for char in strs:
    if 'a' <= char <= 'z':
        answer += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
    elif 'A' <= char <= 'Z':
        answer += chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
    else:
        answer += char

print(answer, end='')  
