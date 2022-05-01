#단지번호 붙이기
import sys
from sys import stdin

n=int(stdin.readline())

acomplex=[]
for _ in range(n): 
    acomplex.append(list(map(int, list(input()))))
print(acomplex)