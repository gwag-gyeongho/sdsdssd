import sys
from sys import stdin
coin=[]
cnt=0
# 정수 두개 입력 받고 화폐 단위 리스트로 입력받기

n, k = map(int,sys.stdin.readline().split())
for i in range(n):
    coin.append(int(stdin.readline()))
i=len(coin)
#k가 0이 될때까지 실행
while k!=0:
    #k가 coin의 [i-1]번째 인덱스에 저장된 값보다 크다면 
    #cnt에 k//coin[i-1]값 저장한후 k에 k%coin[i-1] 저장
    if k>=coin[i-1]:
        cnt+=k//coin[i-1]
        k%=coin[i-1]
    #k가 coin의 [i-1]번째 인덱스에 저장된 값보다 크지않다면
    #i=i-1 실행해 다음 인덱스로 넘어감
    elif k<coin[i-1]:
        i-=1

print(cnt)