from sys import stdin

s=1
cnt=0
k = int(stdin.readline())
sta=[]
seq=[]
for _ in range(k):
    num = int(stdin.readline())
    while s<=num:
        
        seq.append("+")
        sta.append(s)
        s+=1
    if sta[-1]==num:
        seq.append("-")
        sta.pop()
    else:
        cnt+=1
if cnt==0:
    for i in seq:
        print(i)
else:
    print("NO")