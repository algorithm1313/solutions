# 총 검사 시각 -> (N +1) *60 *60 개? (0시0초 ~ N시 59분 59초)
#시각을 나타내는 문자열 안에 K가 하나라도 있으면 카운트
#시,분,초를 모두 for문..? 넘 많이 돌리는거 아닌가아ㅏㅏ

def countK(N,K):
    target = str(K)
    cnt=0 #일단 0값으로 초기화
    
    for H in range(N+1) : #0시 부터 N시 : 시각 H
        for M in range(60) : #60분 M
            for S in range(60) : #60초 S
                totalT=f"{H:02}{M:02}{S:02}"  #?포맷함수?
                if target in totalT:
                        cnt+=1
    return cnt
N,K=map(int,input().split())    
print(countK(N,K))