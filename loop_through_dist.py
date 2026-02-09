mydict  = {'name':'amal',
           'age':20,
           'course':'BCA'}

for key , value in mydict.items():
    print(key, ":",value)


# without the items() method
for key in mydict:
    print(key,":",mydict[key])
    


    # out:
    # name : amal
    # age : 20
    # course : BCA