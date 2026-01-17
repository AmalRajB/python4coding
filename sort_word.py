word_str = 'Hello this Is an Example With cased letters'

# word = [i.lower() for i in word_str.split()  ]

words  = []
for i in word_str.split():
    words.append(i.lower())
words.sort()
print(words)

# out:

# ['an', 'cased', 'example', 'hello', 'is', 'letters', 'this', 'with']

