#include<stdio.h>//standard input output
#include<conio.h>//console input output
//control structure if else switch case for loop
//while loop do while
int main(){
    int age = 0;
    printf("Please enter your age::>");
    scanf("%d",&age);//decimal
    if(age==19){
        printf("You are not young %d",age);
    }else if(age==18){
         printf("You are %d",age);
    }
    else if(age<10){
         printf("You are too young %d",age);
    }else {
        printf("You are too smart and intelligent %d",age);
    }
    getch();
    return 0;

}


