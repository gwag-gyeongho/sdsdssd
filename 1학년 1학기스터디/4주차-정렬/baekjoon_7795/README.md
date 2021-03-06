# 7795번 먹을 것인가 먹힐 것인가 

## 문제
심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. A는 자기보다 크기가 작은 먹이만 먹을 수 있다. 예를 들어, A의 크기가 {8, 1, 7, 3, 1}이고, B의 크기가 {3, 6, 1}인 경우에 A가 B를 먹을 수 있는 쌍의 개수는 7가지가 있다. 8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1.

두 생명체 A와 B의 크기가 주어졌을 때, A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000) 

## 출력
각 테스트 케이스마다, A가 B보다 큰 쌍의 개수를 출력한다.

## 예제 입력
```
2
5 3
8 1 7 3 1
3 6 1
3 4
2 13 7
103 11 290 215
```

## 예제 출력
```
7
1
```

## 코드
```
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
```

### CodeReview
처음에는 for문을 3중으로 써 n과 m이 20000까지 늘어나
수가 너무 커지고 하나하나 다 비교를 하다 보니 시간초과가 되었는데
이진탐색 모듈 bisect를 사용하고 직접 하나하나다 비교하지 않고
특정 값의 번호를 반환해서 A가 B보다 큰 쌍의 개수를 구하였다.
나중에는 직접 이진탐색 모듈을 쓰지 않고 해결할수 있는 방법이
없는지 생각해봐야겠다.
