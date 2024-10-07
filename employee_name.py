'''
PYTHON LAB: employee_name.py

 Print out the last name of the second employee.  
 Print out the first name of the first owner.
 Please search through the dictionary below:
'''
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName":  "Jack", "lastName": "Petter"},
           {"firstName":  "Jessy", "lastName": "Petter"}]}

print(d['employees'][1]["lastName"])
print(d['owners'][0]["firstName"])