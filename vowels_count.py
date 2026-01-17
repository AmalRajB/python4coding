sentance =  'amal is a bca student'
vowels = 'aeiou'

sentance.casefold()
sentance.split()

dist = {}

for i in sentance:
    if i in vowels:
        if i not in dist.keys():
            dist[i] = 0
        dist[i]+=1
print(dist)        




