import heapq as h
from sys import stdin
k = int(stdin.readline())
maxHeap=[]
for i in range(k):
    num = int(stdin.readline())
    if len(maxHeap)==0 and num==0:
            print(0)
    elif num==0:
        print(h.heappop(maxHeap)[1])
    else:
        h.heappush(maxHeap,(-num,num))