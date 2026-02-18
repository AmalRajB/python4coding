my_number = 2


def checkprime(val):
    if (val == 0 or val<1 or val == 1 ):
        print('enter a valid number')
        return
    if (val == 2):
        print('number is prime')
        return
    
    elif (val>2):
        flag = False
        for i in range(2, val):
            if(val%i == 0):
                flag = True
                break
        if flag:
            print('number is not prime')
        else:
            print('number is prime')        


checkprime(my_number)       


# finding prime number in a intervel

start = 10
stop  = 30

def checkprimeintervel(val1,val2):
    for i in range(val1, val2+1):
        if i >1:
            for x in range(2,i):
                if(i%x ==0):
                    break
            else:    
                print(i)


checkprimeintervel(start,stop)                    
            

            



        