
i=0
while True:
    op=int(input('Press 1 +: Press 2 -: Press 3 *: Press 4 /: Press 5 % '))
    f_no=int(input('Enter first number: '))
    s_no=int(input('Enter second number: '))
    if(op==1):
       result = f_no + s_no
       print('{} + {} = {}'.format(f_no,s_no,result))
    elif(op==2):
       result = f_no - s_no
       print('{} - {} = {}'.format(f_no,s_no,result))
    elif(op==3):
       result = f_no * s_no
       print('{} * {} = {}'.format(f_no,s_no,result))
    elif(op==4):
       result = f_no / s_no
       print('{} / {} = {}'.format(f_no,s_no,result))
    elif(op==5):
       result = f_no % s_no
       print('{} % {} = {}'.format(f_no,s_no,result))
    else:
       print('Default')
    i+=1