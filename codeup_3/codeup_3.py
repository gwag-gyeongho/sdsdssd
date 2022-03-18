import sys

d=[]

 

for i in range(11) :#10*10크기의 이차원 배열 생성

    d.append([])        

    for j in range(10) :

        d[i].append(0)

 

for i in range(10) : #예제 입력 받기

    d[i]= input().split()

    for j in range(10):

        d[i][j] = int(d[i][j]) #배열에 있는 값들을 정수형으로 바꿔주기  

x=1 # (2,2) 위치에서 시작

y=1

while True:

    if d[x][y]==2: #만약 d[x][y]에 있는 값이 2라면 9로 바꾸고 while문 탈출

        d[x][y]=9

        break

    elif d[x][y+1]==1 and d[x+1][y]==1 :#아래쪽 오른쪽 모두 1이라서 움직일수 없는 경우 d[x][y]를 9로 바꾸고 while문 탈출

        d[x][y]=9

 

        break

   

    elif d[x][y]==0: #만약 d[x][y]가 0인 경우 9로 바꾸기

        d[x][y]=9

   

    if d[x][y+1]==1: #현재 위치의 오른쪽이 1인경우 아래쪽으로 가기

        x+=1

    elif d[x+1][y]==1:#현재 위치의 아래쪽이 1인 경우 오른쪽으로 가기

        y+=1

    elif d[x][y+1]==0 :#현재 위치의 오른쪽이 0인경우 오른쪽으로 한칸 가기

        y+=1

    elif d[x+1][y]==0:#현재 위치의 아래쪽이 0인 경우 아래쪽으로 한칸 가기

        x+=1

       

 

 

for i in range(0,10):# 이차원 배열 결과 출력

    for j in range(0,10):

        print(d[i][j],end=" ")

    print()