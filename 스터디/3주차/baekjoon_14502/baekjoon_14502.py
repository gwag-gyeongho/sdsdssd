import sys
from sys import stdin
from collections import deque


N,M = map(int,sys.stdin.readline().split())
maze=[]

for _ in range(N):
    maze.append(list(map(int, input())))
