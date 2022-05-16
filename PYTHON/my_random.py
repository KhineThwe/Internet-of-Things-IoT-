import random
name=['khine','zar','thwe','TTU']
print(random.random())
print(random.randint(0,9))
print('printing random integer is: ',random.randrange(0,10,2))
print('Select name is:',random.choice(name))
print('Select name is:',random.sample(name,3))
random.seed()
print('Random number from seed',random.random())