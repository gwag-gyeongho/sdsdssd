k=int(input())

for _ in range(k):
    x=input()
    parenthesis=[]
    for i in x:
        if i=="(":
            parenthesis.append(i)
        elif i==")" and parenthesis[-1]=="(":
            parenthesis.append(i)
        elif i==")" and parenthesis[-1]==")":
            print("NO")
            exit()
        print(parenthesis)
    if parenthesis[-1]==")":
        print("YES")