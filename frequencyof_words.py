def frequencyfn():
    str = input("enter the string : ")
    list = str.split()
    dist = {}

    for i in list:
        if i not in dist.keys():
            dist[i] = 0
        dist[i]+=1
    print(dist)

frequencyfn()        
        
