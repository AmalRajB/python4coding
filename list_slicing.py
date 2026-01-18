mylist  = [1,23,4,5,6,78,89,0,2]

# get full list
print(mylist[:])

# start to specific position
print(mylist[:5])

# start form  a specific to end of list
print(mylist[3:])

# slice the value in between specific index
print(mylist[3:7])

# Get the Items at Specified Intervals
print(mylist[2:7:2])


# out:
# [1, 23, 4, 5, 6, 78, 89, 0, 2]
# [1, 23, 4, 5, 6]
# [5, 6, 78, 89, 0, 2]
# [5, 6, 78, 89]
# [4, 6, 89]