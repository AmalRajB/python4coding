number = 20402
def checkpalindrome(number):
    test = str(number)
    res = test[::-1]
    if test == res:
        print('number is palindrome')
    else:
        print('number is not palindrome')    
    
checkpalindrome(number)    


# out

# number is palindrome