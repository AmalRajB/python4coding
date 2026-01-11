def list_to_dist():
    list1  = [1,2,3]
    list2 = ['one','two','three']

    result = dict(zip(list1,list2))
    # displaying in the form of tuple 
    for i in result.items():
        print(i)
    
list_to_dist()    


# out

# (1, 'one')
# (2, 'two')
# (3, 'three')


