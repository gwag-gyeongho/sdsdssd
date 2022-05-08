#ATM
import sys
from sys import stdin
k=int(stdin.readline())
#리스트 형태로 값 입력 받기
N = list(map(int,input().split()))

sum=0
cnt=0
#오름차순으로 정렬하기
N.sort()
#걸리는 최소 시간 구하기
for i in range(k):
    cnt+=N[i]
    sum+=cnt
print(sum)
