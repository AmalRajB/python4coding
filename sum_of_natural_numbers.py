number = 15

def numbersum(num):
    total = 0
    if num<=0:
        print('enter a positive number')
    else:
        while num>0:
            total +=num
            num-=1
        print(total)    
           

numbersum(number)         

# out 

# 120