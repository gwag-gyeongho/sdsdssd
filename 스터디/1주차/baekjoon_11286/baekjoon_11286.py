import heapq as h # 힙 모듈 불러오기
from sys import stdin

k = int(stdin.readline())
wjfHeap=[]#리스트 생성하기
for i in range(k):#k번 반복하기
    num = int(stdin.readline())
    if num!=0:#num이 0이라면 (절댓값num,num)튜플 형태로 리스트안에 집어넣기
        h.heappush(wjfHeap,(abs(num),num))
    
    elif num==0:#num이 0일때 실행
        if len(wjfHeap)==0:#리스트의 크기가 0이라면 0출력하기
            print(0)
        else:#num이 0이고 리스트의 크기가 0이 아닐때 힙의 루트노드를 빼내고 튜플의 1번 인덱스 값 읽기
            print(h.heappop(wjfHeap)[1])