#안테나
import sys
n = int(sys.stdin.readline())
antenna = sorted(list(map(int,sys.stdin.readline().split())))
print(antenna[(n-1)//2])
"""
#테스트 케이스의 개수가 짝수일때 평균에서 1뺀값으로 정하기
if n%2==0:
    print(antenna[int(n//2-1)])
    #테스트 케이스의 개수가 홀수일때 중간 값으로 정하기
else:
    print(antenna[n//2])
    """