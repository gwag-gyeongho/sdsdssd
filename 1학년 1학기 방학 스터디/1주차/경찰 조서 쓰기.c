#include<stdio.h>

int main(){
    char name[256],what[256];
    int age;
    float weight, height;
    
    printf("�̸��� ������?");
    scanf("%s",name,sizeof(name));

    printf("����̿���?");
    scanf("%d",&age);

    printf("Ű�� �󸶿���??");
    scanf("%f",&height);

    printf("�����Դ� �󸶿���??");
    scanf("%f",&weight);

    printf("���� ���˸� ���������?");
    scanf("%s",what,sizeof(what));

    printf("\n\n--------������ ����--------\n\n");
    printf("�̸� : %s\n",name);
    printf("���� : %d\n",age);
    printf("������ : %.2f\n",weight);
    printf("Ű : %.2f\n",height);
    printf("���� : %s\n",what);
}