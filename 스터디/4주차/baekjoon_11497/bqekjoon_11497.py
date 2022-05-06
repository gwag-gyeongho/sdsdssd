#통나무 건너뛰기
import sys
from sys import stdin

t=int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    log =list(map(int, stdin.readline().split()))
    log.sort()
    a = []
    for i in range(n):
        if i%2==0:
            a.insert(0,log[i])
        elif i%2==1:
            a.insert(len(a),log[i])
    cnt=[]
    for i in range(n-1):
        cnt.append(abs(a[i]-a[i+1]))
    print(int(max(cnt)))