names = ['amal','athul','aswin','arun','ajay']

with open('mailtemplate.txt','r',encoding='utf-8') as file:
    template = file.read()

for name in names:
    mail = template.format(name = name)
    print('-----mail-----')
    print(mail)    




# out:

# -----mail-----
# Dear amal,

# We are happy to inform you that you are selected for the Python Internship.

# Best regards,
# HR Team
# -----mail-----
# Dear athul,

# We are happy to inform you that you are selected for the Python Internship.

# Best regards,
# HR Team
# -----mail-----
# Dear aswin,

# We are happy to inform you that you are selected for the Python Internship.

# Best regards,
# HR Team
# -----mail-----
# Dear arun,

# We are happy to inform you that you are selected for the Python Internship.

# Best regards,
# HR Team
# -----mail-----
# Dear ajay,

# We are happy to inform you that you are selected for the Python Internship.

# Best regards,
# HR Team
