nthterm = 3

def fibonaccifn(nthterm):
    n1 = 0
    n2 = 1
    count = 0
    if nthterm <= 0:
        print('enter a positive term')

    elif nthterm == 1:
        print("the  fibonacci sequence is :")
        print(nthterm)

    else:
        print("the  fibonacci sequence is :")
        while  count<nthterm:
            print(n1)
            next_term = n1 + n2
            n1 = n2
            n2 = next_term
            count += 1

fibonaccifn(nthterm)            
                   