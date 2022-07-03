#케빈 베이컨의 6단계 법칙
N, M = map(int, input().split())
# N*N 크기로 배열 먄들고 N으로 채우기
friend = [[N for _ in range(N)] for _ in range(N)]
# 친구 관계 파악
for _ in range(M):
    a,b = map(int, input().split())
    # a 와 b는 서로 연결 되어있으니까 둘 위치 모두 1로 만들기
    friend[a-1][b-1] = 1
    friend[b-1][a-1] = 1


for k in range(N):
    for i in range(N):
        for j in range(N): 
            if i == j:
                friend[i][j] = 0 #자기 자신과는 친구가 되지 못한다
            else:
                friend[i][j] = min(friend[i][j],
                                       friend[i][k] + friend[k][j])

# 각각의 배열의 합 저장
bacon = []
for i in friend:
    bacon.append(sum(i))

# 합이 가장 작은 인덱스 번호 +1해서 출력
print(bacon.index(min(bacon)) + 1)