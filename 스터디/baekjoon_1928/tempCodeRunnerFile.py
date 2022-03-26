import sys
k=int(input())
aaaa=0
for i in range(3):
    a,b=map(int,sys.stdin.readline().split())
    que=list(map(int,input().split()))
    for j in range(1,len(que)+1): 
        if que.count(que[b])>1:
            if que[0]!=max(que):
                que.append(que[0])
                que.remove(que[0])
                if b==0:
                    b=len(que)-1
                elif b!=0:
                    b-=1
            elif que[0]==max(que):
                aaaa=b+1
                break

        elif que.count(que[b])==1:    
            if que[b]!=max(que):
                que.remove(max(que))
            elif que[b]==max(que):
                aaaa=j
                break
    print(aaaa)