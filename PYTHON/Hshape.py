for row in range(7):
    for col in range(5):
        if col==0 or col==4 or (row==3 and (col>0 and col<4)):
          print("*",end="")
        else:
          print(end=" ")
    print(" ")
for row in range(6):
    for col in range(7):
        if (row==0 and col % 3!=0) or (row==1 and col % 3==0) or (row-col==2) or (row+col==8):
            print("*",end="")
        else:
            print(" ",end="")
    print()