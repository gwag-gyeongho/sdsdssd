#게임 개발
from collections import deque
import sys
t=int(input())
game=[]
for _ in range(t):
    game.append(list(map(int,sys.stdin.readline().split())))

for i in game:
    sum=0
    for j in range(1,len(i)):
        if i[j]!=-1:
            sum+=game[j-1][0]
        else:
            sum+=i[0]
        print(sum,"5555")
    print(sum)