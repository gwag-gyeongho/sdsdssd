student_tuple=(('191102',"홍길동","010-1234-5678"),("191103","임꺽정","010-1357-2468"))
student={}

for i in range(len(student_tuple)):
    student[student_tuple[i][0]]=student_tuple[i][1]

while True:
    key=input()
    if key=="-1":
        break
    else:
        print(student[key])