n = int(input())
cnt = 0
chatting_room = set()

for _ in range(n):
    user = input()
    if user == "ENTER":
        cnt += len(chatting_room)
        chatting_room = set()
    else:
        chatting_room.add(user)
cnt += len(chatting_room)
print(cnt)
