real_list = [[1],[2,5,6],[8,9]]
flat_list = []
for sub_list in real_list:
    for val in sub_list:
        flat_list.append(val)
print(flat_list)        


# out:
# [1, 2, 5, 6, 8, 9]