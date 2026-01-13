number  = 153

def armstrong(num):
    length = len(str(num))
    total = 0
    temp = num
    if num<=0:
        print('enter a positive number')
        return
    else:
        while temp >0:
            digit = temp%10
            total += digit **length
            temp = temp//10
    if num == total:
        print('the number is armstrong')
    else:
        print('the number is not armstrong')                 

armstrong(number)

# out

# the number is armstrong