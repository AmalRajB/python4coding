value_list = [1,2,3,2,4,5,3,1]

# method 1
def remove_duplicate1(value):
    result = list(set(value))
    print(result)
remove_duplicate1(value_list) 

# method 2
def remove_duplicate2(value):
    arr = []
    list = value
    for i in list:
        if i not in arr:
            arr.append(i)
    print(arr)
remove_duplicate2(value_list) 


dict = {
    'country':['india','china','japan','china','japan'],
    'names':['amal','arun','anu','amal','arun']
}

# method 3
def remove_duplicate3(dict):
    dict1 ={}
    for key,value in  dict.items():
        dict1[key] = list(set(value))
    print(dict1)
remove_duplicate3(dict)    



# out:

# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# {'country': ['china', 'japan', 'india'], 'names': ['amal', 'arun', 'anu']}



        
