arr = [1,3,2,10,5,6]
sum = 8

def twosum(arr,sum):
    arr.sort()
    left = 0
    right = len(arr)-1

    while(left<right):
        if arr[left]+arr[right]>sum:
            right = right-1
        elif arr[left]+arr[right]<sum:
            left = left+1
        elif arr[left]+arr[right] == sum: 
            print(f'the pair is {arr[left]} and {arr[right]}')

            right = right - 1
            left  = left + 1   

twosum(arr,sum)             


        #  out 

        # the pair is 2 and 6
        # the pair is 3 and 5