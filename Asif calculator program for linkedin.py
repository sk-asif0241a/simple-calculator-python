#Program for Simple Calculator in Python.
a=float(input('Enter the value for a:'))
b=float(input('Enter the value for b:'))
print('These are the symbols for operations...')
print('+.Addition\n-.Subtraction\n*.Multiplication\n/.Division\n%.Modular Division')
choice=input('Enter your choice:')
match(choice):
    case '+':
        print('Addition=',a+b)
    case '-':
        print('Subtraction=',a-b)
    case '*':
        print('Multiplication=',a*b)
    case '/':
        if(b!=0):
            print('Division=',a/b)
        else:
            print('Invalid Input in b value\nPlease Check it Once...')
    case '%':
        if(b!=0):
            print('Modular Division=',a%b)
        else:
            print('Invalid Input in b value\nPlease Check it Once...')
    case _:
        print('Invalid Choice...\nPlease Try again')
    
