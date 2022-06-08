#가장 긴 증가하는 부분 수열
import sys


n=int(input())
partial=list(map(int,sys.stdin.readline().split()))

dp=[1]*n


for i in range(1,n):
    for j in range(0,i):
        if partial[j] < partial[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))