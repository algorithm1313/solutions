'''
    브라ㅇㅜㄴ 가로 = bw
    브라운 세로 = bh
    옐로우 가로 = yw
    옐로우 세로 = yh
    
    1. 브라운 가로, 브라운 세로 길이 = 옐로우 가로+2, 옐로우 세로+2
    bw, bh = (yw + 2), (yh + 2)
    
    2. 브라운 + 옐로우 = 카펫 전체 크기 = 브라운 가로 x 브라운 세로
    brown + yellow = carpet = bw x bh = (yw + 2) x (yh + 2)
    
    C. 옐로우 = 옐로우 가로 x 옐로우 세로 
    yellow = yw x yh = (bw - 2) x (bh - 2)
    
    D. 브라운 = ㅈㅓㄴㅊㅔ-ㅇㅖㄹㄹㅗㅇㅜ 
    '''


def solution(brown, yellow):
    total = brown + yellow # 전체 카펫 크기 
    for bh in range(3, total):  # 최소 높이는 3부터 
        if total % bh == 0:
            bw = total // bh
            if (bw - 2) * (bh - 2) == yellow: # 테두리 빼고 계산하기!
                return (bw, bh)



# def solution(brown, yellow):
    
#         # 1. 세로 길이는 가로보다 작거나 같다는 조건이 있으므로 절반까지 확인
#     for bh in range(1, brown//2 + 1):
        
#         # 2. 가로, 세로 구하기ㅜㅜ
#         bw = (brown - 2 * bh + 4)
#         yw, yh = bw - 2, bh - 2
        
#         # 3. 옐로우 = 옐로우 가로 x 옐로우 세로 이면서 옐로우 + 브라운이 브라운 가로 x 브라운 세로를 만족하면
#         if yellow == yw * yh and yellow + brown == bw * bh:
            
#             # 4. 브라운 가로, 브ㅔ라운 세로가 카펫의
#             return [bw, bh]