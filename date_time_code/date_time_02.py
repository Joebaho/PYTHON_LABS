'''
PYTHON LAB: date_time_02.py

Convert string into a datetime object
For example, You received the following date in string format. Please convert it into Python’s DateTime
object
date_string = "Feb 25 2020 4:20PM"

'''
from datetime import datetime
date_string="Feb 25 2020 4:20PM"
date_time_obj=datetime.strptime(date_string,"%b %d %Y %H:%M%p")
print(date_time_obj)
