def solution(board, moves):
    answer = 0
    stack = []
    a=0
    for i in moves:
        move = i-1
        for j in range(len(board)):
            if board[j][move] != 0:
                a = board[j][move]
                board[j][move] = 0
                if stack and stack[-1] == a:
                    stack.pop()
                    answer+=2
                else : stack.append(a)
                break
    return answer