#include<stdio.h>//standard input output
#include<conio.h>//console input output
//control structure if else switch case for loop
//while loop do while
int main(){
    int btData = 0;
    while(1<10){
    printf("Reading Bluetooth Data::>");
    scanf("%d",&btData);//decimal
    switch(btData){

    case 1:
         printf("Car is moving forward\n");

    break;
    case 2:
          printf("Car is moving backward\n");
    break;
    case 3:
          printf("Car is moving left\n");
    break;
    case 4:
         printf("Car is moving right\n");
    break;
    case 5:
          printf("Car is stop\n");
    break;
    }
    }
    getch();
    return 0;

}


