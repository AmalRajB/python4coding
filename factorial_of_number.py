number = 7
factorial = 1
if number<0:
    print("factorial of a negateive number is not defined")
elif number == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,number+1):
        factorial = factorial*i
    print(f'the factorial of {number} is {factorial}')            


# out:

# the factorial of 7 is 5040