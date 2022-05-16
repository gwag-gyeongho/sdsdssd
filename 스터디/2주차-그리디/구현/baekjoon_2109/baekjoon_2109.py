#순회강연
import sys
from sys import stdin
import heapq as h
# 강의 수를 입력 받고 강의의 마감일과 강의료 리스트 형태로 입력 받기
lecture=[]
k=int(stdin.readline())
for _ in range(k):
    lecture.append(list(map(int,input().split())))

cnt=0
deadline=1
#0번 인덱스 기준으로 정렬 한후 1번 인덱스 기준으로 다시 정렬하기
lecture.sort()
lecture.sort(key = lambda x: x[1]) 

money=[]
# 최소 힙을 사용해서 강연료가 낮은 강연은 빼내기
for i in lecture:
  h.heappush(money, i[0])
  if (len(money)>i[1]):
    h.heappop(money)

sum=0
#money 리스트에 있는 돈 다 더해주기
for i in money:
    sum+=i
print(sum)