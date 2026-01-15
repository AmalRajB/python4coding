def factorialfn(n):
    if n<=1:
        return n
    else:
        return n * factorialfn(n-1)
    
number = -1

if number<=0:
    print('invalid output..')
else:
    print(f'the factorial is : { factorialfn(number)}')
