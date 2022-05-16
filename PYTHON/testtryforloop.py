for i in range(5):
    print('_____')
    try:
        z=10/(i-3)
        print('z= ',z)
    except ZeroDivisionError:
        print('Divided by zero')
    finally:
        print('always run')
    print(i)