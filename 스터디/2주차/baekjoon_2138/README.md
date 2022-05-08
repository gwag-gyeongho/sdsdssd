# 2138 전구와 스위치

## 문제
N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.

N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.

## 입력
첫째 줄에 자연수 N(2 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 전구들의 현재 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 그 다음 줄에는 우리가 만들고자 하는 전구들의 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 0은 켜져 있는 상태, 1은 꺼져 있는 상태를 의미한다.

## 출력
첫째 줄에 답을 출력한다. 불가능한 경우에는 -1을 출력한다.

## 예제 입력
```
3
000
010
```

## 예제 출력
```
3
```
## 코드
```
import sys


# 전구의 상태 바꿈
def switch_button(num):
    if num == 0:
        num = 1
    else: num = 0

    return num


# 전구 스위치
def switch(state, cnt):
    # 첫번째 전구 스위치를 눌렀을 때 첫번째 전구와 두번째 전구의 상태를 바꿔준다.
    if cnt == 1:
        state[0] = switch_button(state[0])
        state[1] = switch_button(state[1])
    # 반복문을 통해 전구의 상태를 확인한다.
    for i in range(1, n):
        # 스위치 이전에 전구의 상태와 바꿔야하는 전구의 상태를 비교
        if state[i-1] != after[i-1]:
            cnt += 1
            # 이전 전구와 스위치 전구의 상태를 바꾼다.
            state[i-1] = switch_button(state[i-1])
            state[i] = switch_button(state[i])

            # 스위치 이후에 전구가 있다면 이후 전구의 상태를 바꾼다.
            if i != n-1:
                state[i+1] = switch_button(state[i+1])

    # 현재 전구의 상태와 바꿔야하는 전구의 상태가 같으면 멈춘다.
    if state == after:
        return cnt

    # 바꿔야하는 전구의 상태로 바꾸지 못하므로 -1 출력
    else:
        return -1

n = int(sys.stdin.readline())
now = list(map(int,sys.stdin.readline().rstrip("\n")))
after = list(map(int,sys.stdin.readline().rstrip("\n")))

res1 = switch(now[:], 0) # 첫번째 전구 스위치를 안누르고 시작한 경우
res2 = switch(now[:], 1) # 첫번째 전구 스위치를 누르고 시작한 경우

# 2가지 조건으로 했을 때 더 작은 횟수를 출력
if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
    
# 0보다 큰 횟수를 출력
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
    
# 둘다 0보다 작기때문에 -1 출력
else:
    print(-1)
```


### CodeReview

이 문제도 행렬 문제와 비슷하게 어려워서 다른 사람의 코드를 참고하였다.

케이스 두개를 생각해야하고 내가 생각했을때 경우의 수가 너무 많아 코드를 어떻게
짤찌 막막했다. 위와 같이 실제로 실행하는 코드는 짧은데 사용자 정의함수의 길이가
되게 길다. 이 문제도 스터디 조원들과 함께 얘기 해보면서 문제에 대해 완전히 이해하지는
못했지만 이해도를 높였다.






