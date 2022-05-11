import sys
from sys import stdin

n,m = map(int,sys.stdin.readline().split())

array = list(map(int,sys.stdin.readline().split()))
#이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

#이진탐색 수행
result = 0
while (start<=end):
    total = 0
    mid = (start + end)//2
    for i in array:
        # 잘랐을 때의 나무의 양 계산
        if i> mid:
            total+= i - mid
    # 나무의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total<m:
        end = mid -1
    # 나무의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:# 최대한 덜 잘랐을때가 정답이므로, 여기에서 result 에 기록
        result = mid 
        start = mid + 1
print(result)

"""
n,m = map(int,sys.stdin.readline().split())

tree = list(map(int,stdin.readline().split()))
cnt=0

k=max(tree)
sum=0
while True:
    cnt=0
    for i in range(n):
        if tree[i]>k:
            cnt=cnt+tree[i]-k
        if cnt == m:
            break

    if cnt == m:
        break
    else:
        k-=1

print(k)
"""