import sys
from sys import stdin
coin=[]
cnt=0
n, k = map(int,sys.stdin.readline().split())
for i in range(n):
    coin.append(int(stdin.readline()))
i=len(coin)
while k!=0:

    if k>=coin[i-1]:
        cnt+=k//coin[i-1]
        k%=coin[i-1]
       
    elif k<coin[i-1]:
        i-=1

print(cnt)