#include<stdio.h>

int main(){
    char name[256],what[256];
    int age;
    float weight, height;
    
    printf("이름이 뭐에요?");
    scanf("%s",name,sizeof(name));

    printf("몇살이에요?");
    scanf("%d",&age);

    printf("키는 얼마에요??");
    scanf("%f",&height);

    printf("몸무게는 얼마에요??");
    scanf("%f",&weight);

    printf("무슨 범죄를 저질렀어요?");
    scanf("%s",what,sizeof(what));

    printf("\n\n--------범죄자 정보--------\n\n");
    printf("이름 : %s\n",name);
    printf("나이 : %d\n",age);
    printf("몸무게 : %.2f\n",weight);
    printf("키 : %.2f\n",height);
    printf("범죄 : %s\n",what);
}