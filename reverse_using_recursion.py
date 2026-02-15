def str_rev(s):
    if len(s) == 0:
        return s
    return str_rev(s[1:]) + s[0]

my_string = "amal"
print(f'the reverse of the string {my_string} is {str_rev(my_string)}')