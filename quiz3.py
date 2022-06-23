with open("num.txt","r") as fd:
    s=list(fd.read().split('\n'))
    


k=[]
for i in s:
    k.append(i.split(" "))
k.pop(0)
x=[]
for i in k:
    x.append(list(map(int,i)))
    
x.sort()

for i in x:
    for j in i:
        print(j,end=" ")
    print()