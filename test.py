#소수 출력

while True:
    num1=int(input("***첫 번째 숫자를 입력하세요 :"))
    num2=int(input("***두 번째 숫자를 입력하세요 :"))
    if num1 >=2:
        for i in range(num1,num2):
            a=0
            for j in range(2,i):
                if i%j==0:
                    a+=1
            if a==0:
                print(i)
        break
    else:
        print("첫번째 숫자를 1보다 큰 숫자를 입력하세요")
    
    