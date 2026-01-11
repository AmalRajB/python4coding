word = "w1 a"

def word_reverse(word):
    length  = len(word)
    if length == 1:
        print(word)
        return

    word2 = word.split(' ')
    size  = len(word2)
    rev_all = ""

    for i in range(size):
        rev = word2[i]
        rev_all = rev+" "+rev_all
    result = rev_all.strip()   
    print(result)    








word_reverse(word)