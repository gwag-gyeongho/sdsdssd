#안테나
import sys
from sys import stdin
from collections import deque

n = int(stdin.readline())
antenna = list(map(int, stdin.readline().split()))
antenna.sort()

#테스트 케이스의 개수가 짝수일때 평균에서 1뺀값으로 정하기
if n%2==0:
    print(antenna[int(n//2-1)])
    #테스트 케이스의 개수가 홀수일때 중간 값으로 정하기
else:
    print(antenna[n//2])