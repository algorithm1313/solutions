def solution(numbers, hand):
    answer = ''

    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    left_pos = keypad['*']
    right_pos = keypad['#']
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_pos = keypad[number]
        elif number in [3, 6, 9]:
            answer += 'R'
            right_pos = keypad[number]
        else:
            num_pos = keypad[number]
            left_dist = abs(left_pos[0] - num_pos[0]) + abs(left_pos[1] - num_pos[1])
            right_dist = abs(right_pos[0] - num_pos[0]) + abs(right_pos[1] - num_pos[1])
            
            if left_dist < right_dist:
                answer += 'L'
                left_pos = num_pos
            elif right_dist < left_dist:
                answer += 'R'
                right_pos = num_pos
            else:
                if hand == "left":
                    answer += 'L'
                    left_pos = num_pos
                else: 
                    answer += 'R'
                    right_pos = num_pos
                    
    return answer
