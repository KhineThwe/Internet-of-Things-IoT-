def add(a,b):  #function header a,b=parameter
    return a+b
def sub(a,b):  
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
fdata=int(input("Enter first number: "))
sdata=int(input("Enter second number: "))
print("Adding: ",add(fdata,sdata))
print("Subtrating: ",sub(fdata,sdata))
print("Multiplying: ",multi(fdata,sdata))
print("Dividing: ",div(fdata,sdata))