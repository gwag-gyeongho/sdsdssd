n,m = map(int,sys.stdin.readline().split())
#리스트 만들기
maze=[]
#리스트 안에 n번 만큼 리스트 넣기
for _ in range(n):
    maze.append(list(map(int, input())))