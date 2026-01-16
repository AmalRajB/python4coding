m1 = [
    [1,2,4],
    [4,3,5],
    [5,7,2]
]

m2 = [
    [4,6,2],
    [9,7,3],
    [0,5,1]
]

result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]


for i in range(len(m1)):
    for j in range(len(m1[0])):
        result [i][j] = m1[i][j] + m2[i][j]

for res in result:
    print(res)        

# out:
# [5, 8, 6]
# [13, 10, 8]
# [5, 12, 3]
