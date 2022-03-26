import sys
k=int(input())#반복할 횟수 입력
aaaa=0
for i in range(k):
    a,b=map(int,sys.stdin.readline().split())# a,b에 각각 정수 입력 받기
    que=list(map(int,input().split()))#큐 입력 받기
    aaaa=0
    while True: #무한반복하기
        if que[0]==max(que):#리스트의 첫번째에 있는 인덱스가 리스트 안에 있는 수들 중 최대값이라면 실행
            aaaa+=1
            if b==0: #만약 0번째 인덱스가 최댓값이면서 b가 0이라면 멈추기
                break
            else:#b가 0이 아니라면 b의 0번째 인덱스 삭제하기
                que.pop(0)
            if b==0:#리스트 안의 값이 조정됨에 따라 b값도 같이 바꿔주기
                b=len(que)-1
            else:
                b-=1
                
        else: # 리스트의 첫번째 인덱스가 최댓값이 아닌경우 첫번째 인덱스 값 맨 뒤로 보내기
            que.append(que[0])
            que.remove(que[0])
            if b==0:#리스트 안의 값이 조정됨에 따라 b값도 같이 바꿔주기
                b=len(que)-1
            else:
                b-=1

    print(aaaa)# 큐의 b번째에 있는 인덱스 값이 몇번째로 프린트 되었는지 출력