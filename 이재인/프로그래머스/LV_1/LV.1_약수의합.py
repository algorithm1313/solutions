Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(n):
...     answer=0
...     for i in range(1, n+1):
...         if n%i ==0:
...             answer+=i
...     return answer
