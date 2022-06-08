num = list(input())
i=1
sum=0
def eliminate(num):
    num.pop(i-1)
    num.pop(i-1)
    num.pop(i-1)

def brak(num):
    
    k=num.index("(")
    if num[k+2]=="+":
        result=int(num[k+1])+int(num[k+3])
    elif num[k+2]=="-":
        result=int(num[k+1])-int(num[k+3])
    elif num[k+2]=="*":
        result=int(num[k+1])*int(num[k+3])
    elif num[k+2]=="/":
        result=int(num[k+1])/int(num[k+3])
    for _ in range(5):
        num.pop(k)
    num.insert(k,result)
    return result




while True:

    

    if "(" in num:

        brak(num)
    else:
        if num[i]=="*":
                sum+=int(num[i-1])*int(num[i+1])
                eliminate(num)
                num.insert(i-1,sum)


        elif num[i]=="/":
                sum+=int(num[i-1])/int(num[i+1])
                eliminate(num)
                num.insert(i-1,sum)


        elif "*" not in  num and "/" not in num:
            if num[i]=="+":
                sum+=int(num[i-1])+int(num[i+1])
                eliminate(num)
                num.insert(i-1,sum)

            elif num[i]=="-":
                    sum+=int(num[i-1])-int(num[i+1])
                    eliminate(num)
                    num.insert(i-1,sum)

        if i<len(num)-1:
            i+=1
        else:
            i=0
        if len(num)==1:
            break
        sum=0
       



print(sum)