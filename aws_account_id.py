#This Code we will be using string format and flows work to extract the aws account Id from a arn

#Declaration of Variables
arn="arn:aws:iam::123456789012:user/Development/product_1234/*"
owner= "Depes"
account_id = arn[13:25]
sentence1 = f"Hello {owner}," "\n" 
sentence2 = " The AWS account_id you are looking is: {}. " .format(account_id)

# Print the sentence
print(sentence1, sentence2)

