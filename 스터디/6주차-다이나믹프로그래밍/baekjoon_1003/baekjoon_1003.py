# 피보나치 함수
t = int(input())
 
for _ in range(t):
    fib0 = [1,0]
    fib1 = [0,1]
    n = int(input())
    if n>1:
        for i in range(n-1):
            fib0.append(fib1[-1])
            fib1.append(fib0[-2]+fib1[-1]) 

    print(fib0[n],fib1[n])
