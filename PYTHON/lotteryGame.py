import secrets
import sys
secureNumber=secrets.SystemRandom()
while True:
    print('___Welcome to our game___')
    press1=int(input('Press 1 to Read rule or Press 2 to play the game:>'))
    if press1==1:
        print('>>Age > 18 only allowed<<')
        print('>>Show money more than 5000<<')
        print('>>You must use more than 1000 each time<<')
    if press1==2:
        userName=input('Please enter your name:>')
        userAge=int(input('Please enter your age:>'))
        while len(userName)>2 and userAge>17:
            print('You can play now!!!')
            print('Welcome:>',userName)
            while True:
                userMoney=int(input('Please enter your show money:>'))
                while userMoney>4999:
                    while True:
                        print('This is your show money:$',userMoney)
                        inputMoney=int(input('Please enter money to play:>'))
                        luckynumber=int(input('Please enter your lucky number:>'))
                        systemNumber=secureNumber.randint(10,99)
                        if luckynumber==20:
                            print('You are win in 2D Game')
                            userMoney=(inputMoney*10)+(userMoney-inputMoney)
                            print('This is your all money:>',userMoney)    
                            toQuit=int(input('Press 0 to play again!!!'))
                            if toQuit!=0:
                                sys.exit('Bye Bye')
                            else:
                                continue
                        print('Try again....Lucky number is ',systemNumber)
                        userMoney=userMoney-inputMoney
                        if userMoney<1000:
                            print('You have not enough money!!!',userMoney)
                            break
                
                print('Please More Money^^')

        print('Please read the rule again!!!')
       