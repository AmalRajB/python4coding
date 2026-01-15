def recursionfn(n):
    if n<=1:
        return n
    else:
        return n + recursionfn(n-1)

number = 16
if number<=0:
    print('invalid input...')
else:
    print(f'the sum is : {recursionfn(number)}')        
