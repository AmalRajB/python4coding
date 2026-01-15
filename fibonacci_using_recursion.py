def recursionfn(n):
    if n<=1:
        return n
    else:
        return recursionfn(n-1) + recursionfn(n-2)
    
nthterm = 10
if nthterm<=1:
    print('enter a valid term...')
else:

    print('the fibonacci sequance is :')
    for i in range(nthterm):
        print(recursionfn(i))


#     out:

#     the fibonacci sequance is :
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34