print("Press 1:For add")
print("Press 2:For subtract")
print("Press 3:For multiply")
print("Press 4:For divide")
userInput=int(input("Enter something: "))
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

if userInput == 1:
    result=firstNumber + secondNumber
elif userInput == 2:
    result=firstNumber - secondNumber
elif userInput == 3:
    result=firstNumber * secondNumber
elif userInput == 4:
    result=firstNumber / secondNumber
else:
    print("You must enter 1/2/3/4")
print("The result is ",result)
    
