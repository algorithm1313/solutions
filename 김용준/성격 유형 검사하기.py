def solution(survey, choices):
    scores = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    character = {'R':0, 'T':0, 'C':0, 'F':0,
                'J':0, 'M':0, 'A':0, 'N':0}

    for survey_one, choice in zip(survey, choices):
        if choice > 4:
            character[survey_one[1]] += scores[choice]
        elif choice == 4:
            continue
        else:
            character[survey_one[0]] += scores[choice]
            
    answer = ''
    if character['R'] < character['T']:
        answer += 'T'
    else:
        answer += 'R'
    if character['C'] < character['F']:
        answer += 'F'
    else:
        answer += 'C'
    if character['J'] < character['M']:
        answer += 'M'
    else:
        answer += 'J'
    if character['A'] < character['N']:
        answer += 'N'
    else:
        answer += 'A'
    return answer
