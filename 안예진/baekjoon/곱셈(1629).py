#자연수 A를 B번 곱한 수를 알고 싶다.
#단 구하려는 수가 매우 커질 수 있으므로 
#이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
import sys

def solution(A,B,C):
    return pow(A,B,C)

A, B, C = map(int, input(). split())  
print(solution(A,B,C))