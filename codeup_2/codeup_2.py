import sys #모듈 불러오기

candy=[] # 배열 생성

a,b = map(int,sys.stdin.readline().split()) # 정수 a,b에 입력 받기

for i in range(a+1) : # a*b 크기의 이차원 배열(격자판) 생성

    candy.append([])        

    for j in range(b+1) :

        candy[i].append(0)

 

k=int(input())

# l-막대의 길이/d-막대를 놓는 방향/x,y-막대를놓는가장왼쪽 or 위쪽 위치

#d - 0가로 1세로

for i in range(k): #k번 만큼 반복

    l,d,x,y,= map(int,sys.stdin.readline().split())

    if d==0: #d가 0이라면 candy[x][y]위치를 기준으로 가로에 있는 0을 1로 바꿈

        for j in range(l):

            candy[x][y+j]=1

       

    else : #d가 0이 아니고 다른것이면 candy[x][y]위치를 기준으로 세로에 있는 0을 1로 바꿈

        for j in range(l):

            candy[x+j][y]=1

 

for i in range(1,a+1): #이차원 배열 결과 출력

    for j in range(1,b+1):

        print(candy[i][j],end=" ")

    print()