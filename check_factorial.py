my_number = 10

factorial = 1

for i in range(1 , my_number+1):
    factorial = factorial*i

print(factorial)

# recursion

def find_factorial(val):
    if val<=1:
        return val
    else:
        return val * find_factorial(val-1)
        

print(f'factorial is {find_factorial(my_number)}')
