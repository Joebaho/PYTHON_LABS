'''
PYTHON LAB: aws_account_id.py

Write a program that will display the account id from the arn below:
arn:aws:iam::123456789012:user/Development/product_1234/*
Display on the screen: the aws account id is: account_id.'''

#This Code we will be using string format and flows work to extract the aws account Id from a arn

#Declaration of Variables
arn="arn:aws:iam::123456789012:user/Development/product_1234/*"
owner= "Depes"
account_id = arn[13:25]

sentence1 = f"Hello {owner}," "\n" 
sentence2 = " The AWS account_id you are looking is: {}. " .format(account_id)

# Print the sentence
print(sentence1, sentence2)

# spliting the ARN string using ':' as the separator

arn_parts = arn.split(':')

# the account ID will be the 5th element(index4) in the resulting list:

account_id2 = arn_parts[4]
# Deplay result:
print(f" the arn splitting is {arn_parts} \n")
print(f"The aws account id is {account_id2}")

