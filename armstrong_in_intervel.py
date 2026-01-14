start = 100
end = 500

def armstrongs(start,end):
    for num in range(start,end+1):
        length = len(str(num))
        total = 0
        temp = num
        while temp>0:
            digit = temp%10
            total +=digit ** length
            temp//=10
        if total == num:
            print(num)
armstrongs(start,end)                

# out 

# 153
# 370
# 371
# 407