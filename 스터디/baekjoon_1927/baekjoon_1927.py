import heapq as h #힙 모듈 불러오기
from sys import stdin

minHeap=[]#리스트 만들기
k = int(stdin.readline())
for i in range(k):#k번 반복하기
    num = int(stdin.readline())
    
    if len(minHeap)==0 and num==0:#만약 리스트의 크기가 0이고 num이 0이라면 0 출력하기
        print(0)
    elif num==0: #num이 0이라면 minHeap에서 루트 노드에서 최소 값 빼내고 출력하기
        print(h.heappop(minHeap))
    else:#num이 0이 아니라면 minHeap에 num넣기
        h.heappush(minHeap,num)
    