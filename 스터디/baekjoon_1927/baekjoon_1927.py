import heapq as h
from sys import stdin

minHeap=[]
k = int(stdin.readline())
for i in range(k):
    num = int(stdin.readline())
    
    if len(minHeap)==0 and num==0:
        print(0)
    elif num==0:
        print(h.heappop(minHeap))
    else:
        h.heappush(minHeap,num)
    