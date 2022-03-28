from sys import stdin
k = int(stdin.readline())
mHeap=[]
for i in range(k):
    num = int(stdin.readline())
    if num == 0:
        if len(mHeap)==0:
            print(0)
        else:
            
            print(mHeap.pop(0))
    else:
        mHeap.append(num)   
        mHeap.sort(reverse=True)