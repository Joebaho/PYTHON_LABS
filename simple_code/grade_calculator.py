'''
PYTHON LAB: grade_calculator.py

Write a program that will ask a student for their grades in 5 subjects.
Calculate your average grade and print grade from A-E.
A>90
B>80
C>70
D>60
E===Failed

Display on the screen:  Provide the screenshot and github link.  Submit your homework in your github account as well.  Create a folder in Python-codes
'''
name = str(input("Please provide the student name:\t"))
level = str(input("Please enter the student class: \t"))
Eng_grade = float(input("Please enter your grade score for English:\t"))
Math_grade = float(input("Please enter your grade score for Mathematic:\t"))
Labs_grade = float(input("Please enter your grade score for Labs:\t\t"))
Tf_grade = float(input("Please enter your grade score for Terraform:\t"))
Py_grade = float(input("Please enter your grade score for Python:\t"))
# Grade adjectives
A = "Excellent"
B = "Good"
C = "Average"
D = "Below Average"
E = "Poor"
F = "Failing"
#operations 
total_grade = Eng_grade + Math_grade + Labs_grade + Tf_grade + Py_grade
result = total_grade / 5
print(f"Student Name:\t {name.upper()}")
print(f"Class Name: \t{level.capitalize()}")
print(f"Total Grade:\t {total_grade:.2f}")
#conditional statement
if result >= 90:
    print(f"GPA :{result:.2f} \t Grade : A")
    print(f"Congratulation you have passed with \033[1m{A.upper()}\033[0m distinction")
elif result >= 80 and result < 90:
    print(f"GPA : {result:.2f} \t Grade : B")
    print(f"Congratulation you have passed with \033[1m{B.upper()}\033[0m distinction")
elif result >= 70 and result < 80:
    print(f"GPA : {result:.2f} \t Grade : C")
    print(f"Congratulation you have passed with \033[1m{C.upper()}\033[0m distinction")
elif result >= 60 and result < 70:
    print(f"GPA : {result:.2f} \t Grade : D")
    print(f"Sorry you have failed with \033[3m{D.upper()}\033[0m distinction")
else:
    if result < 60:
        print(f"GPA : {result:.2f} \t Grade : E")
        print(f"Sorry you have failed with \033[3m{E.upper()}\033[0m distinction")