#단지번호 붙이기
import sys
from sys import stdin
from collections import deque

sum=0
cnt=0
# 함수 만들기
def dfs (x,y):
    global sum
    if x <= -1 or y <= -1 or x >= n or y >= n:
        
        return False
    
    elif int(acomplex[x][y]) == 1:
        acomplex[x][y] = 0
        sum +=1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

n=int(stdin.readline())

acomplex=[]
for _ in range(n): 
    acomplex.append(list(map(int, list(input()))))

apartment=[]
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            cnt += 1
            apartment.append(sum)
            sum=0
apartment.sort()
print(len(apartment))
for i in apartment:
    print(i)