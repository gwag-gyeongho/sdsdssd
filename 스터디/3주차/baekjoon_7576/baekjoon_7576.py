#토마토
import sys
from sys import stdin
from collections import deque



n,m = map(int,sys.stdin.readline().split())
box=[]

for _ in range(m):
    box.append(list(map(int,stdin.readline().rstrip().split())))
print(box)

