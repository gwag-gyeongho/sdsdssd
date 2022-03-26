import sys
k=int(input())
aaaa=0
for i in range(k):
    a,b=map(int,sys.stdin.readline().split())
    que=list(map(int,input().split()))
    aaaa=0
    while True:
        if que[0]==max(que):
            aaaa+=1
            if b==0:
                break
            else:
                que.pop(0)
            if b==0:
                b=len(que)-1
            else:
                b-=1
                
        else:
            que.append(que[0])
            que.remove(que[0])
            if b==0:
                b=len(que)-1
            else:
                b-=1

    print(aaaa)