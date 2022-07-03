import sys
k, n = map(int,sys.stdin.readline().split())
lan=[]
for i in range(k):
    lan.append(int(sys.stdin.readline()))
lan.sort()
start,end = 0, lan[-1]

while sum != n:
    mid = (start + end) // 2
    sum=0
    for i in range(k):
        sum+=lan[i]//mid
    if sum <= n:
        end = mid 
        a = mid
    else:
        start = mid 

print(a)