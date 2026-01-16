panctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_string = "amal; ;is! !!a.. --.student"

no_punch = ''

for char in my_string:
    if char not in panctuations:
        no_punch = no_punch+char
print(no_punch)        


