import sys
from sys import stdin
import bisect 

t=int(stdin.readline())
for _ in range(t):
    cnt=0
    a,b = map(int,sys.stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    B = list(map(int, stdin.readline().split()))
    A.sort()
    print(A)
    print(bisect.bisect(A, 8))