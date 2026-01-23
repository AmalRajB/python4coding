my_list1 = ['a',1,4,'e']
my_list2 = ['b',5,100,'x']

# method 1

joined_list = my_list1 + my_list2
print(joined_list)

# method 2

for x in my_list2:
    my_list1.append(x)
print(my_list1)    

# method 3

my_list1.extend(my_list2)
print(my_list1)

# out

# ['a', 1, 4, 'e', 'b', 5, 100, 'x']