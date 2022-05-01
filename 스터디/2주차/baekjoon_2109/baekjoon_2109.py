import sys
from sys import stdin
import heapq as h
lecture=[]
k=int(stdin.readline())
for _ in range(k):
    lecture.append(list(map(int,input().split())))
cnt=0
deadline=1
lecture.sort()
lecture.sort(key = lambda x: x[1]) 
print(lecture)
money=[]
for i in lecture:
  h.heappush(money, i[0])
  if (len(money)>i[1]):
    h.heappop(money)
sum=0
for i in money:
    sum+=i
print(sum)