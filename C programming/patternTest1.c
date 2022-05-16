#include<stdio.h>//standard input output
#include<conio.h>
int main(){
    int i,j,n;
    //printf("Enter number of rows: ");
    //scanf("%d",&n);
    for(i=1;i<=5;i++){//2=5
        for(j=1;j<=i;j++){
            printf("%d",j);
        }
        printf("\n");
    }
    return 0;

}
//1
//12
//123
//1234
//12345
