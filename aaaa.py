print("음료수를 선착하세요")
k=int(input("0=콜라 500원/1=사이다 800원/2=환타 1200원\n"))
num=int(input("돈을 넣으세요\n"))
if k==0:
    num-=500
elif k==1:
    num-=800
elif k==2:
    num-=1200

print("거스름돈:")
print("5000원:",num//5000,"개")
num=num%5000
print("1000원:",num//1000,"개")
num=num%1000
print("500원:",num//500,"개")
num=num%500
print("100원:",num//100,"개")
num=num%100