import sys
input=sys.stdin.readline

score=[]
for _ in range(5):
    score.append(list(map(int,input().split())))
print(score)
num=1
cook=0
cook=sum(score[0])
for i in range(1,5):
    if sum(score[i])>cook:
        cook=sum(score[i])
        num=i+1
print(num,cook)