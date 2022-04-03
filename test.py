k=[0,1]

n = int(input())

for i in range(n-1):
    k.append(k[i]+k[i+1])
print(k[-1])