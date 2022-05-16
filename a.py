def base8(num):
    if num>0:
        return base8(num//8)+str(num%8)
num=int(input())
print(base8())
    