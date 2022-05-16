data1=input("Please enter number: ")
data2=input("Please enter number: ")
if(data1>data2):
    print('{} is greater than {}'.format(data1,data2))
elif(data1==data2):
    print('{} is equal to {}'.format(data1,data2))
else:
    print('{} is greater than {}'.format(data2,data1))