import sys
from sys import stdin
from collections import deque
#bfs 함수 만들기
def bfs (x,y):
    #deque 양방향 큐 만들기
    que = deque()
    que.append((x,y))

    while que:
        x,y = que.popleft()
        #상하좌우 살피기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #리스트의 범위를 벗어나면 걔속 진행
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            #리스트의 값이 0이면 계속 진행
            if maze[nx][ny] == 0:
                continue
            #리스트의 값이 1이라면 최단거리 기록
            if maze[nx][ny]==1:
                maze[nx][ny] = maze[x][y]+1
                que.append((nx,ny))

    return maze[n-1][m-1]
#정수 두개 입력 받기
n,m = map(int,sys.stdin.readline().split())
#리스트 만들기
maze=[]
#리스트 안에 n번 만큼 리스트 넣기
for _ in range(n):
    maze.append(list(map(int, input())))



dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs(0,0))