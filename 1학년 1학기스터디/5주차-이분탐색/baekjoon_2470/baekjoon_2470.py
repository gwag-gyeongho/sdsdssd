import sys
from sys import stdin


n=int(stdin.readline())

a=list(map(int,stdin.readline().split()))
a.sort(key = abs)


cnt=abs(a[0]+a[1])
x,y=a[0],a[1]


for i in range(n-1):
    if abs(cnt)>abs(a[i]+a[i+1]):
        
        cnt=abs(a[i]+a[i+1])

        x,y=a[i],a[i+1]
        
b=[]
b.append(x)
b.append(y)
b.sort()
for i in range(2):
    print(b[i],end=" ")