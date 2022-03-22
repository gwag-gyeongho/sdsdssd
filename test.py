import sys
from sys import stdin
num = int(input())
asdf=[]
for i in range(num):
    que = sys.stdin.readline().split()
    if que[0]=="push":
        asdf.append(que[1])
    elif que[0]=="pop":
        if len(asdf)!=0:
            print(asdf[0])
            asdf.pop(0)
        else:
            print(-1)
    elif que[0]=="size":
        print(len(asdf))
    elif que[0]=="empty":
        if len(asdf) ==0:
            print(1)
        else:
            print(0)
    elif que[0]=="front":
        if len(asdf)==0:
            print(-1)
        else:
            print(asdf[0])
    elif que[0]=="back":
        if len(asdf)==0:
            print(-1)
        else:
            print(asdf[len(asdf)-1])
    que.clear()