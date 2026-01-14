
def calculator():

    options = [1,2,3,4]

    while True:
        try:
            number1 = int(input('enter the first number : '))
            number2 = int(input('enter the second number : '))
            operation = int(input('select operation:\n1(addition)\n2(substraction)\n3(multiplication)\n4(division)\n>'))

        except ValueError:
            print('enter a valid number')
            continue

        if operation not in options:
            print('select valid operation...')
            continue

        if operation == 1:
            print(number1+number2)
        elif operation == 2:
            print(number1-number2)
        elif operation == 3:
            print(number1*number2)
        elif operation == 4:
            print(number1/number2)

        nxt = input('if you waant to continue ? "yes" "no" : ')
        if nxt == 'no':
            break
        else:
            continue    

calculator()        

