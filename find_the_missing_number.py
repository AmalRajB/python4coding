list = [1,2,3,4,6,7,8]

def missingnumfn(list):
    
    n = list[-1]
    sumof_list = 0
    total = n*(n+1)//2
    sumof_list = sum(list)
    missing_num = total-sumof_list
    print(missing_num)

    # for i in range(min(list),max(list)+1):
    #     if i not in list:
    #         print(i)

missingnumfn(list)


# out

# 5