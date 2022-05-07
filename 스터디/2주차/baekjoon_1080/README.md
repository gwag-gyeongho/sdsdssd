# 1080 행렬

## 문제
0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

## 입력
첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

## 출력
첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.

## 예제 입력 
```
3 4
0000
0010
0000
1001
1011
1001
```

## 예제 출력 
```
2
```

## 코드
```
n, m = map(int, input().split()) 
listA = []
for _ in range(n): # 리스트A 선언
    listAc
listB = []
for _ in range(n): # 리스트B 선언
    listB.append(list(map(int, list(input()))))


def check(i, j): # 뒤집기 함수
    for x in range(i, i+3):
        for y in range(j, j+3):
            if listA[x][y] == 0:
                listA[x][y] = 1
            else:
                listA[x][y] = 0


cnt = 0 # 카운트
if (n < 3 or m < 3) and listA != listB:
    # 예외 1, 리스트가 작을 때
    cnt = -1
else:
    for r in range(n-2):
        for c in range(m-2):
            if listA[r][c] != listB[r][c]:
                cnt += 1
                check(r, c)

if cnt != -1:
    if listA != listB: # A와 B가 같은지 확인
        cnt = -1
print(cnt)
```

### CodeReview
이 문제는 혼자 풀기에는 너무 여려운것 같아서 
다른 블로그에 문제 풀이를  참고 했다.
뒤집기 함수를 만들어내느냐 못만들어 내느냐가
핵심인문제다. 그리고 예외도 생각 해줘야 하는 문제라서 어려웠다.
그래서 조원들끼리 이야기를 많이 나누어본 문제다.






