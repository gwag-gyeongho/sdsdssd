#종언아 고마워
import sys
n = int(sys.stdin.readline())
v = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

l, r = 0, v[-1]

if sum(v) < m:
    print(r)
    exit()

while l <= r:
    mid = (l + r) // 2
    if sum(min(mid, x) for x in v) <= m:
        l = mid + 1
        a = mid
    else:
        r = mid - 1

print(a)