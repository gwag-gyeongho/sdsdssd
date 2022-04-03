import sys
from sys import stdin
k=int(stdin.readline())
N = list(map(int,input().split()))

sum=0
cnt=0
N.sort()
for i in range(k):
    cnt+=N[i]
    sum+=cnt
print(sum)
