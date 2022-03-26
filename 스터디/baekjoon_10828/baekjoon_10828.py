import sys
from sys import stdin
num = int(input())
asdf=[]
for i in range(num):
    sta = sys.stdin.readline().split()
    if sta[0]=="push":
        asdf.append(sta[1])
    elif sta[0]=="pop":
        if len(asdf)!=0:
            print(asdf.pop(len(asdf)-1))
        else:
            print(-1)
    elif sta[0]=="size":
        print(len(asdf))
    elif sta[0]=="empty":
        if len(asdf) ==0:
            print(1)
        else:
            print(0)
    elif sta[0]=="top":
        if len(asdf)==0:
            print(-1)
        else:
            print(asdf[len(asdf)-1])
    sta.clear()
