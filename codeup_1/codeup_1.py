d=[]             #리스트 생성      

for i in range(19) : #이차원 배열 만들기

    d.append([])        

    for j in range(19) :

        d[i].append(0)

       

for i in range(19) :

    d[i]=input().split() #예제 입력 받기

 

 

 

n = int(input()) # 십자 뒤집기 횟수 입력

for i in range(n) : #앞에서 입력받은 횟수 만큼 반복

    x,y=input().split() #x 와 y에 값 입력받아 저장

    x=int(x)-1 #배열의 첫번째 인덱스가 0이므로 -1하기

    y=int(y)-1

    for j in range(19) :

       

        if int(d[j][int(y)])==0 : #d[j][y]에 입력된 숫자가 0이면 1로 바꾸기

            d[j][int(y)]=1

        else:

            d[j][int(y)]=0 # 1이라면 0으로 바꾸기

       

    for j in range(19):

        if int(d[int(x)][j])==0 :#d[x][j]에 입력된 숫자가 0이면 1로 바꾸기

            d[int(x)][j]=1

        else:

            d[int(x)][j]=0 # 1이라면 0으로 바꾸기

 

 

for i in range(0,19): # 이차원 배열에서 십자 뒤집기 한 결과 출력하기

    for j in range(0,19):

        print(d[i][j],end=" ")

    print()