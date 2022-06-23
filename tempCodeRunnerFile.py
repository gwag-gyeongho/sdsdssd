import sys

d=[]

for i in range(0,20):
    for j in range(0,i):
        d.append(i)

a,b=map(int,sys.stdin.readline().split())
print(sum(d[a-1:b]))