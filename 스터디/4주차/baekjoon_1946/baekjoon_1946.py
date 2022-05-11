#신입사원 
import sys
from sys import stdin
#테스트 할 횟수 입력 받기
t= int(stdin.readline())
# t번만큼 반복하기
for _ in range(t):
    fm=[]
    #신입사원이 몇명인지 입력받기
    n = int(stdin.readline())
    #이차원 리스트 만들기
    for _ in range(n):    
        fm.append(list(map(int,stdin.readline().split())))
    #첫번째 인덱스 기준으로 정렬하기
    fm.sort()
    #a에 fm[0][1]정렬하기
    a=fm[0][1]
    cnt=1
    #리스트의 길이만큼 반복하기
    for i in range(1,len(fm)):
        # a에 저장된 값이 fm의[i][1]보다 크다면 cnt에 1 더해주고 a의 값 바꿔주기
        if a>fm[i][1]:
            cnt+=1
            a=fm[i][1]

    print(cnt)