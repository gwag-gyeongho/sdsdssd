# 2667번 단지번호붙이기
## 문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



## 입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

## 출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

## 예제 입력 
```
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```
## 예제 출력 
```
3
7
8
9
```
## 코드
```
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
#리스트 오름차순으로 정렬
apartment.sort()
#총 단지 수 가 몇개인지 출력
print(len(apartment))
#단지마다 크기가 얼마인지 출력
for i in apartment:
    print(i)
 
 ```
 
 
 
 
 ### CodeReview
 이 문제도 비슷한 문제 풀이가 3강 문제 풀이에 있어서 3강 문제 풀이를 참고하여 풀었다.
 이 문제를 풀면서 어렴풋이 BFS와 DFS에 대해 알게 된것 같지만 아직까지 잘 이해가 되지 않아
 어렵다.
 
 
 
 
