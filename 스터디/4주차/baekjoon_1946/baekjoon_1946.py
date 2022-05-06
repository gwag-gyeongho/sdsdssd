import sys
from sys import stdin

t= int(stdin.readline())

for _ in range(t):
    fm=[]
    n = int(stdin.readline())
    for _ in range(n):    
        fm.append(list(map(int,stdin.readline().split())))
    fm.sort()

    a=fm[0][1]
    cnt=1
    for i in range(1,len(fm)):
        if a>fm[i][1]:
            cnt+=1
            a=fm[i][1]

    print(cnt)
