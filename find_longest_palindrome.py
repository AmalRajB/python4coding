def longest_palindrome(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i,len(s)):
            sub_str = s[i:j+1]
            if sub_str == sub_str[::-1]:
                if len(sub_str)>len(longest):
                    longest = sub_str
    return longest

my_string = "amalrajb" 
print(longest_palindrome(my_string))


# out :
#    ama

           
