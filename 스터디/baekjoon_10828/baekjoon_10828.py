import sys
from sys import stdin
num = int(input())#반복할 횟수 입력 받기
asdf=[]#빈 리스트 생성
for i in range(num):
    sta = sys.stdin.readline().split()#입력 받기
    if sta[0]=="push":# "push"뒤에 따라 나오는 숫자 리스트에 추가
        asdf.append(sta[1])
    elif sta[0]=="pop":# "pop"뒤에 따라 나오는 숫자 리스트에서 없애고 그 수 출력
        if len(asdf)!=0:
            print(asdf.pop(len(asdf)-1))
        else:#만약 리스트가 비어 있다면 -1출력
            print(-1)
    elif sta[0]=="size":#리스트의 크기 출력
        print(len(asdf))
    elif sta[0]=="empty":#리스트가 비어있지 않다면 0출력 비어있다면 1 출력
        if len(asdf) ==0:
            print(1)
        else:
            print(0)
    elif sta[0]=="top":#스택의 맨 위에 있는 숫자 출력하기 리스트가 비어있다면 -1출력
        if len(asdf)==0:
            print(-1)
        else:
            print(asdf[len(asdf)-1])
    sta.clear()#리스트 초기화 하기
