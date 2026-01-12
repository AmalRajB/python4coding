number = 407

def checkprime(val):
    if val == 0 or val == 1:
        print('number is not a prime')
        return
    elif(val>1):
        flag = False
        for i in range(2,val):
            if(val%i == 0):
                flag = True
                break
        if flag:
            print('the number is not prime')
        else:
            print(f'{val} is a prime number')  

checkprime(number)    


# checking a the prime number in an intervel

start = 10
end = 30

def checkprimes(start,end):
    for num in range(start,end+1):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                print(num)
checkprimes(start,end)                    