s = input()
answer = ""


for char in s:  
    if char.isalpha():  
        if char.islower():  
            answer += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif char.isupper():  
            answer += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
    else:
        answer += char  
answer += " "  

print(answer)  