import heapq as h #힙 모듈 불러오기
from sys import stdin
k = int(stdin.readline())
maxHeap=[]#리스트 만들기
for i in range(k):#k번 반복하기
#heqpq 모듈은 최소 힙 밖에 지원안하기 때문에 튜플 형태(-num,num)로 값을 리스트안에
#입력받아
    num = int(stdin.readline())
    if len(maxHeap)==0 and num==0:#maxHeap의 크기가 0이고 숫자가 0이라면 0출력하기
            print(0)
    elif num==0:#num이 0이라면 maxhHeap 루트 노드 값을 빼내고 튜플안에 양수 값 출력하기
        print(h.heappop(maxHeap)[1])
    else:
        h.heappush(maxHeap,(-num,num))#튜플 형태로 리스트에 갑 입력받기
        print(maxHeap)