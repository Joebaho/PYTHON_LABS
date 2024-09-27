#Program for grade calculator
name = str(input("Please provide the student name:\t"))
level = str(input("Please enter the student class: \t"))
grade1 = float(input("Please enter your grade score for English:\t"))
grade2 = float(input("Please enter your grade score for Mathematic:\t"))
grade3 = float(input("Please enter your grade score for Labs:\t\t"))
grade4 = float(input("Please enter your grade score for Terraform:\t"))
grade5 = float(input("Please enter your grade score for Python:\t"))
# Grade adjectives
A = "Excellent"
B = "Good"
C = "Average"
D = "Below Average"
E = "Poor"
F = "Failing"
#operations 
total_grade = grade1 + grade2 + grade3 + grade4 + grade5
result = total_grade / 5
print(f"Student Name:\t {name.upper()}")
print(f"Class Name: \t{level.capitalize()}")
print(f"Total Grade:\t {total_grade}")
#conditional statement
if result >= 90:
    print(f"GPA :{result} \t Grade : A")
    print(f"Congratulation you have passed with \033[1m{A.upper()}\033[0m distinction")
elif result >= 80 and result < 90:
    print(f"GPA : {result} \t Grade : B")
    print(f"Congratulation you have passed with \033[1m{B.upper()}\033[0m distinction")
elif result >= 70 and result < 80:
    print(f"GPA : {result} \t Grade : C")
    print(f"Congratulation you have passed with \033[1m{C.upper()}\033[0m distinction")
elif result >= 60 and result < 70:
    print(f"GPA : {result} \t Grade : D")
    print(f"Sorry you have failed with \033[3m{D.upper()}\033[0m distinction")
else:
    if result < 60:
        print(f"GPA : {result} \t Grade : E")
        print(f"Sorry you have failed with \033[3m{E.upper()}\033[0m distinction")