def solution(board, moves):
    stack = []
    answer = 0

    for m in moves:
        # print(f"{m}번째 인형뽑기")
        for i in range(len(board)):
            if board[i][m-1] != 0:
                # print(f"{i+1}번째 인형있음")
                if stack and stack[-1] == board[i][m-1]:
                    answer += 2
                    # print("동일한 인형 발견 answer =",answer)
                    stack.pop()
                    print(stack)
                    board[i][m-1] = 0
                    break
                else:
                    stack.append(board[i][m-1])
                    board[i][m-1] = 0
                    # print(stack, "추가되었음")
                    break
    return answer

# board = [[0,0,0,0,0],
#          [0,0,1,0,3],
#          [0,2,5,0,1],
#          [4,2,4,4,2],
#          [3,5,1,3,1]]
# moves = [1,5,3,5,1,2,1,4]

# print(solution(board,moves))