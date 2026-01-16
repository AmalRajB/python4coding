number = 20402
def checkpalindrome(number):
    test = str(number)
    res = test[::-1]
    if test == res:
        print('number is palindrome')
    else:
        print('number is not palindrome')    
    
checkpalindrome(number)  

# other options

value = 'aIbohPhoBiA'
value = value.casefold()
res = reversed(value)

if list(value) == list(res):
    print('palindrome')
else:
    print('not palindrome')    



# x = ''.join( list(res))
# print(x)




# out

# number is palindrome