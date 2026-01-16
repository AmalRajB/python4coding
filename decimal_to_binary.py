def des_to_bin(n):
    if n > 1:
        des_to_bin(n//2)
    print(n%2,end='')

number = 76
des_to_bin(number) 
       

# out:

# 1001100