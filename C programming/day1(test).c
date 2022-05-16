#include<stdio.h>//standard input output
#include<conio.h>//console input output
//control structure if else switch case for loop
//while loop do while
int main(){
    int btData = 0;
    int id=0;
    int passcode=0;
    int count=0;//assignment operator
    //== ka relational operator
while(count<3){
    printf("Please enter your id::>");//standard input
    scanf("%d",&id);//standard output
    printf("Please enter your pass-code::>");
    scanf("%d",&passcode);
    while( id==123 && passcode==1234){
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
    default :
         printf("Car is out of service\n");
    break;
    }

    }
    printf("Try again\n");
    count++;

    }
    printf("You must be a ScriptKiddie");
    getch();
    return 0;

}



