#통나무 건너뛰기
import sys
from sys import stdin
#테스트 케이스 횟수 입력받기
t=int(stdin.readline())
#t번만큼 반복하기
for _ in range(t):
    n = int(stdin.readline())
    #리스트 형태로 입력받기
    log =list(map(int, stdin.readline().split()))
    #오름차순으로 정렬하기
    log.sort()
    a = []
    #가장 작은 값이 중간에 오도록 리스트 다시 만들기
    for i in range(n):
        if i%2==0:
            a.insert(0,log[i])
        elif i%2==1:
            a.insert(len(a),log[i])

    cnt=[]
    #리스트의 양 옆 인덱스마다 차를 구해서 절댓값이 가장 큰 수 출력하기
    for i in range(n-1):
        cnt.append(abs(a[i]-a[i+1]))
    print(int(max(cnt)))