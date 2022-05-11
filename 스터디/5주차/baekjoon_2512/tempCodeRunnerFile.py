import sys
from sys import stdin
import bisect

n=int(stdin.readline())

budget=list(map(int,sys.stdin.readline().split()))

total = int(sys.stdin.readline())

budget.sort()

start=budget[0]
end=budget[-1]

result=(start+end)//2

if sum(budget)<=total:
    print(budget[-1])
else:
    while sum(budget)>total:
      
        del budget[bisect.bisect(budget,result):n]
        for i in range(bisect.bisect(budget,result),n):
            budget.append(result)
        if sum(budget)>total:
            result-=1

    print(result)