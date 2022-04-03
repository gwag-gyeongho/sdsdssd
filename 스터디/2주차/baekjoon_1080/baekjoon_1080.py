import sys
from sys import stdin

matrix=[]         
n,m = map(int,sys.stdin.readline().split())      

for i in range(n) :
    matrix.append([])         
    for j in range(m) : 
        matrix[i].append(0)
print(matrix)
for i in range(2*m) :
    matrix[i]=input().split()
print(matrix)

