import sys
from sys import stdin
import heapq as h
lecture=[]
k=int(stdin.readline())
for _ in range(k):
    lecture.append(list(map(int,sys.stdin.readline().split())))
lecture.sort()


classroom=[]
h.heappush(classroom,lecture[0][1])
for i in range(1, k): 
    if lecture[i][0] < classroom[0] :  
        h.heappush(classroom,lecture[i][1])
    else:
        h.heappop(classroom)
        h.heappush(classroom,lecture[i][1])
        
print(len(classroom))