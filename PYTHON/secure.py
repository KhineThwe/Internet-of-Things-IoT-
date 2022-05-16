import secrets
print('Printing integer from secrets module')
secureGenerator = secrets.SystemRandom
numberList = [1,2,3,4,77,8]
randomNumber = secureGenerator.randint(0,10)
randomNumber1 = secureGenerator.randrange(0,50,4)
randomNumber2 = secureGenerator.choice(numberList)
print('Secure random number is',randomNumber)
print('Secure randrange number is',randomNumber1)
print('Secure choice number is',randomNumber2)