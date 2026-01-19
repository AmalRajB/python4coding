my_dict = {
    'key1':4,
    'key2':5,
    'key3':1,
    'key4':3
    
}

items = list(my_dict.items())

# helper function
def sort_value(item):
    return item[1]

items.sort(key = sort_value)

sorted_dict = {}

for key , value in items:
    sorted_dict[key] = value

print(sorted_dict)    

# out:
# {'key3': 1, 'key4': 3, 'key1': 4, 'key2': 5}