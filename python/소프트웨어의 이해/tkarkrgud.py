#헤론의 공식
import math

print('삼각형 세 변의 길이 입력')
a=int(input())
b=int(input())
c=int(input())
s=(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('삼각형의 면적 %s'%area)
