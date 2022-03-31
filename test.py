l=[]
for i in range(9):
    k=int(input())
    l.append(k)

print(max(l))
print(l.index(max(l))+1)