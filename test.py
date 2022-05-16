def base2 (num):
    if num<1:
        return "0"
    elif num==1:
        return "1"
    if num%2==0:
        return base2(int(num/2))+"0"
    elif num%2 == 1:
        return  base2(int(num/2))+ "1"

def  base8 (num):
    if num<8:
        return str(num)
    elif num==8:
        return "1"
    if num%8==0:
        return base2(int(num/8))+"0"
    elif num%8 != 0:
        return  base2(int(num/8))+ str(num%8)

def base16 (num):
    if num<10:
        return str(num)
    elif num==10:
        return "A"
    elif num==11:
        return "B"
    elif num==12:
        return "C"
    elif num==13:
        return "D"
    elif num==14:
        return "E"
    elif num==15:
        return "F"
    elif num==16:
        return "10" 

    if num%16 ==0:
        return base2(int(num/16))+"0"
    elif num%16 < 10:
        return  base2(int(num/16))+ str(num%16)
    elif num%16 == 10:
        return base2(int(num/16))+"A"
    elif num%16 == 11:
        return base2(int(num/16))+"B"
    elif num%16 == 12:
        return base2(int(num/16))+"C"
    elif num%16 == 13:
        return base2(int(num/16))+"D"
    elif num%16 == 14:
        return base2(int(num/16))+"E"
    elif num%16 == 15:
        return base2(int(num/16))+"F"

num= int(input("10진수 입력--> "))
print("2진수: ",base2(num))
print("8진수: ",base8(num))
print("16진수: ",base16(num))

