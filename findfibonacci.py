nth_term = 6

n1 = 0
n2 = 1

count = 0

if (nth_term>1):
    while count<nth_term:
        print(n1)   
        next_term = n1 + n2
        n1 = n2
        n2 = next_term
        count +=1


