import sys
from sys import stdin

t= int(stdin.readline())

for _ in range(t):
    fm=[]
    n = int(stdin.readline())
    for _ in range(n):    
        fm.append(list(map(int,input().split())))
    fm.sort()
    c=n
    for i in range(1,n):
        if fm[0][1]<fm[i][1]:
            c-=1
    print(c)