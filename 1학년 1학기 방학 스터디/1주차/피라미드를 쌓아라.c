#include<stdio.h>

int main(){
    int floor;
    printf("�� ������ �װڴ��� ");
    scanf("%d",&floor);
    for(int i=0;i<floor;i++){
        for(int j=floor;j>i;j--){
            printf(" ");
        }
        for(int k=0;k<i*2+1;k++){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}