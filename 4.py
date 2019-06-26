#        4. Days Calculator
from datetime import datetime
print("Date format dd/mm/yy")
date1 = input("enter 1st date:")
date2 = input("enter 2nd date:")
date_format = "%d/%m/%Y"
a = datetime.strptime(date1, date_format)
b = datetime.strptime(date2, date_format)
delta = b - a
x = (delta.days)
print("There are ",  x, " days in between",  date1 ," and ",date2 )