#집합의 표현
import sys
sys.setrecursionlimit(10**6)


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def find_parent(parent,x):
	#루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

a, b = map(int, sys.stdin.readline().split())

root = [0] * (a + 1)

for i in range(a + 1):
    root[i] = i

for _ in range(b):
    c, d, f = map(int, sys.stdin.readline().split())
    if c == 0:
        union_parent(root, d, f)
    elif c == 1:
        if find_parent(root, d) == find_parent(root, f):
            print("YES")
        else:
            print("NO")