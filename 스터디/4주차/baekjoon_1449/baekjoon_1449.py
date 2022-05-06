import sys
from sys import stdin
#두 정수 입력 받기
n,l = map(int,sys.stdin.readline().split())
#리스트 형태로 수리 할 곳 입력 받기
pipe = list(map(int, stdin.readline().split()))
#리스트 오름차순으로 정렬하기
pipe.sort()

sum=0
cnt=1
#n-1번 만큼 반복하기
for i in range(n-1):
    #테이프의 길이가 sum+pipe[i+1]-pipe[i]+1보다 크거나 같다면 실행
    if sum+pipe[i+1]-pipe[i]+1<=l:
        sum=sum+pipe[i+1]-pipe[i]
    # if문의 조건에 성립하지 않는다면 sum 초기화 하고 cnt에 1더해주기
    else:
        sum=0
        cnt+=1
print(cnt)