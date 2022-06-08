import os
try:
    with open("./aaa/hello.txt","x") as fd:
        s=fd.read()
        print(s)
except FileExistsError:
    with open("./aaa/hello.txt","r") as fd:
        s=fd.read()
    k=len(os.listdir("./aaa"))-1
    with open("./aaa/hello_copy_{0}.txt".format(k),"x") as fd:
        fd.write(s)