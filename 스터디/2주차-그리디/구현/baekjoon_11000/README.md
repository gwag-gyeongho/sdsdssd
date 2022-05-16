# 11000 강의실 배정

## 문제
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!

## 입력
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

## 출력
강의실의 개수를 출력하라.

## 예제 입력 
```
3
1 3
2 4
3 5
```

## 예제 출력 
```
2
```

## 코드 
```
import sys
from sys import stdin
import heapq as h

lecture=[]
k=int(stdin.readline())
for _ in range(k):
    lecture.append(list(map(int,sys.stdin.readline().split())))
lecture.sort()


classroom=[]
h.heappush(classroom,lecture[0][1])
for i in range(1, k): 
    if lecture[i][0] < classroom[0] :  
        h.heappush(classroom,lecture[i][1])
    else:
        h.heappop(classroom)
        h.heappush(classroom,lecture[i][1])

print(len(classroom))
```

### CodeReview
이 문제는 전 강의시간의 끝나는 시간과 다음 강의의 시작하는 시간이 다르다면
강의실을 하나 더 써야하기 때문에 그 부분을 구현하기가 어려웠다. 
최소힙을 활용해서 이 부분을 해결했다. 전 강의시간의 끝나는 시간과 다음 강의의 시작하는 시간을 비교해
다음 강의가 시작하는 시간이 전 강의 시간의 끝나는 시간보다 작다면 힙을 사용해 리스트안에 푸쉬하고
그렇지 않다면 원래시간을 팝해서 빼내고 새로운 시간을 푸쉬 해 넣는다
