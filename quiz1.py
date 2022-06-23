person1=["온달",20,1,180.0,100.0]
person2=["이사부",25,1,170.0,70.0]
person3=["평강",22,0,169.0,60.0]
person4=["혁거세",40,1,150.0,50.0]

personlist=person1+person2+person3+person4
def how_many_persons(personlist):
    cnt=len(personlist)//5
    
    return cnt

def compute_average_age(personlist):
    cnt=0
    for i in range(1,len(personlist),5):
        cnt+=personlist[i]
   
    return cnt//how_many_persons(personlist)

def count_males_females(personlist):
    male=0
    female=0
    for i in range(2,len(personlist),5):
        if personlist[i]==1:
            male+=1
        else:
            female+=1

    return male ,female

def display_persons(personlist):
    for i in range(0,len(personlist),5):
        print(personlist[i:i+5])

n_person=how_many_persons(personlist)
average_age=compute_average_age(personlist)
n_male,n_female=count_males_females(personlist)




print("사람 수:",n_person)
print("평균나이:",average_age)
print("남자:",n_male,", 여자:",n_female)
display_persons(personlist)
