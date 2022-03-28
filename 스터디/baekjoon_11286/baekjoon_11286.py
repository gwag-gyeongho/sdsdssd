import heapq as h
from sys import stdin

k = int(stdin.readline())
wjfHeap=[]
for i in range(k):
    num = int(stdin.readline())
    if num!=0:
        h.heappush(wjfHeap,(abs(num),num))
    
    elif num==0:
        if len(wjfHeap)==0:
            print(0)
        else:
            print(h.heappop(wjfHeap)[1])