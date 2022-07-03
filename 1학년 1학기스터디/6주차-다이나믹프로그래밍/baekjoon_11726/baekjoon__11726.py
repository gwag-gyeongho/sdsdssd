#2xN 타일링

d=[0] * 1003


d[1]=1
d[2]=2
n=int(input())


for i in range(3,1001):
	d[i] = d[i-1] + d[i-2]
print(d[n]%10007)
