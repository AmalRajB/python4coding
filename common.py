letter1 = input("enter the first word :")
letter2 = input("enter the second word :")

def commanfn(letter1,letter2):
    ltr1 = set(letter1)
    ltr2 = set(letter2)
    comman = ltr1 & ltr2
    com = ltr1.intersection(ltr2)
    print(comman)
    print(com) 

commanfn(letter1,letter2)
    