for row in range(7):
    for col in range(5):
        if (row==0 and (col >=0 and col<5)) or (col==2 and (row >=0 and row<7)) :
                 print("*",end="")
        else:
          print(end=" ")
    print(" ")