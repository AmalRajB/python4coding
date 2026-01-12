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