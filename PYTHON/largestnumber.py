#largest number program
a=110
b=200
c=300
d=1000
if(a>b) and (a>c) and (a>d):
    largestNumber = a
elif(b>a) and (b>c) and (b>d):
    largestNumber = b
elif(c>a) and (c>b) and (c>d):
    largestNumber = c
else:
    largestNumber = d
print('largest Number is ',largestNumber)