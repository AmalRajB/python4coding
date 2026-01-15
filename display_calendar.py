import calendar

mm = int(input('enter the month : '))
yy = int(input('enter the year : '))

def display_calendar(mm,yy):
    print((calendar.month(yy,mm)))

display_calendar(mm,yy)    



# out

#    February 2026
# Mo Tu We Th Fr Sa Su
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28