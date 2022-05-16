#include<stdio.h>//standard input output
#include<conio.h>
int main(){
    int i,j,n;
    //printf("Enter number of rows");
    //scanf("%d",&n);
    for(i= 5;i>=1;i--){
        for(j=1;j<=i;j++){
            printf("%d",j);
           // printf("#");
        }
        printf("\n");
    }
    return 0;
}
//12345
//1234
//123
//12
//1
