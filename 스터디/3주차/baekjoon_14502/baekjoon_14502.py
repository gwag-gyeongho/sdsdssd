import sys
from sys import stdin
from collections import deque


n,m = map(int,sys.stdin.readline().split())
lab=[]

for _ in range(n):
    lab.append(list(map(int,stdin.readline().rstrip().split())))

