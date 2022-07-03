#먹을것인가 먹할것인가
import sys
from sys import stdin
import bisect
# *이진탐색* 오름차순 정렬되어 있는 리스트에서 원하는 값을 빠르게 찾을 수 있음

# 반복할 횟수 입력 받기
t=int(stdin.readline())
for _ in range(t):
    cnt=0
    #숫자 입력 받기
    a,b = map(int,sys.stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    B = list(map(int, stdin.readline().split()))
    #A와 B 오름차순으로 정렬하기
    A.sort()
    B.sort()
    #A에 정렬되어 있는 숫자-1 하여 그 숫자의 위치가 어디있는지 반환후 cnt에 저장
    for i in A:
        cnt+= bisect.bisect(B,i-1)
    #결과 출력
    print(cnt)