year = 2024

def chek_leep_year(year):
    if(year%400 == 0) and (year%100 == 0):
        print(f'{year} is a leep year')

    elif(year%4 == 0) and (year%100 !=0):
        print(f'{year} is a leep year') 

    else:
        print(f'{year} is not a leep year') 

chek_leep_year(year)


# out

# 2024 is a leep year


# leep years in an interver

start = 2000
end = 2020

def checkleep(start,end):
    for yer in range(start,end+1):
        if (yer%400 ==0) and (yer%100 ==0):
            print(yer)
        elif (yer%4 == 0) and (yer%100 !=0):
            print(yer)
        else:
            pass
checkleep(start,end)               

# out

# 2000
# 2004
# 2008
# 2012
# 2016
# 2020

