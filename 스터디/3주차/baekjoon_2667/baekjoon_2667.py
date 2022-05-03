#단지번호 붙이기
import sys
from sys import stdin
from collections import deque

sum=0
cnt=0
# 함수 만들기
def dfs (x,y):
    #전역변수 생성
    global sum
    #리스트의 범위를 벗어나면 false를 반환
    if x <= -1 or y <= -1 or x >= n or y >= n:
        
        return False
    #리스트에 저장된 값이 1이라면 실행
    elif int(acomplex[x][y]) == 1:
        acomplex[x][y] = 0
        sum +=1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
#리스트 크기 입력
n=int(stdin.readline())

acomplex=[]
#리스트 입력받기
for _ in range(n): 
    acomplex.append(list(map(int, list(input()))))

apartment=[]
#단지 수 계산하기
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            cnt += 1
            apartment.append(sum)
            sum=0
#리스트 내림차순으로 정렬
apartment.sort()
#총 단지 수 가 몇개인지 출력
print(len(apartment))
#단지마다 크기가 얼마인지 출력
for i in apartment:
    print(i)