from sys import stdin

s=1
k = int(stdin.readline())
sta=[0]
seq=[]
for i in range(k):
    num = int(stdin.readline())
    seq.append(num)

for i in range(seq[0]):
    sta.append(s)
    s+=1
    print("+")
print("-")

for i in range(1, len(seq)):
    if seq[i]>seq[i-1]:
        sta.append(s)
        print("+\n"*(seq[i]-seq[i-1]))
        s+=1
    else :
        sta.pop()
        print("-")
    


        