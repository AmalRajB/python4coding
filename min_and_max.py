list = [10,34,32,55,7,33,56,77,9,100]

# for finding the max value
def findmax(list):
    size = len(list)
    max_value = list[0]

    for i in range(size):
        if list[i]>max_value:
            max_value = list[i]
    print(f'max value is : {max_value}')

findmax(list)    

# for finding the minimum value
def findmin(list):
    size = len(list)
    min_value = list[0]

    for i in range(size):
        if list[i]<min_value:
            min_value = list[i]
    print(f'min value is : {min_value}')

findmin(list)   

# out 

# max value is : 100
# min value is : 7