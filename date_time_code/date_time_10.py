'''
PYTHON LAB: date_time_10.py

 Calculate number of days between two given dates
Given:
#2020-02-25
date_1 = datetime(2020, 2, 25)
#2020-09-17
date_2 = datetime(2020, 9, 17)
Expected output:
205 days

'''
from datetime import datetime

# Given dates
date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)

# Calculate the difference between the two dates
date_diff = date_2 - date_1

# Print the number of days between the two dates
print(f"{date_diff.days} days")

######################################################

# 2020-02-25
date_1 = datetime(2020, 2, 25).date()
# 2020-09-17
date_2 = datetime(2020, 9, 17).date()
delta=None
if date_1>date_2:
   delta=date_1-date_2
else:
   delta=date_2-date_1
print("Difference of the days will be: \n",delta.days)