'''
PYTHON LAB: string_18.py

extract the email service provider name

'''
# First solution
email = "john.smith@example.com"
provider = email.split("@")[1].split(".")[0]
print(provider)

#Second Solution
emaillist=["KSR@datavizion.com","mymail@yahoo.com","milindmali@google.com","snehal@health.edu"]
for i in emaillist:
   i=i.replace("@",".").split(".")
print(i[1])