#가장 긴 증가하는 부분 수열
import sys


n=int(input())
partial=list(map(int,sys.stdin.readline().split()))
partial.sort()
a=partial[0]
cnt=1
for i in partial:
    if a<i:
        cnt+=1
        a=i
print(cnt)