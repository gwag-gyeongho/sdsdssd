import sys
from sys import stdin
k=int(stdin.readline())
meeting=[]
for _ in range(k):
    meeting.append(list(map(int,input().split())))       #이차원 배열으로 회의 시간 입력 받기
meeting.sort()     #0번 인덱스 기준으로 정렬하기
meeting.sort(key = lambda x: x[1])#1번 인덱스 기준으로 정렬하기

sum = 1 
conference = meeting[0][1] 
for i in range(1, k): 
    if meeting[i][0] >= conference : 
        sum += 1 
        conference  = meeting[i][1]
print(sum)

    