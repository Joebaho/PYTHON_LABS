'''
PYTHON LAB: athlete_lap_assignment.py

Objective: Practice using loops to iterate through a list and display information.
Task: Write a Python program that uses a list of four U.S. women athletes who have competed in the 400 meters at the Olympics. Your program should do the following:
Create a list called athletes with the following names:
Allyson Felix
Sanya Richards-Ross
Shaunae Miller-Uibo
Phyllis Francis
Use a for loop to display each athlete's name along with the lap number they completed. The output should be in the following format:
Lap 1: Allyson Felix has completed their lap!
Lap 2: Sanya Richards-Ross has completed their lap!
Lap 3: Shaunae Miller-Uibo has completed their lap!
Lap 4: Phyllis Francis has completed their lap!
Requirements:
Do not use the enumerate() function.
Use a counter variable to keep track of the lap number.
Bonus Challenge:
Modify your code to display a message at the end that says: "All athletes have completed their laps!"

'''

# Create a list of athletes
athletes = [
    "Allyson Felix",
    "Sanya Richards-Ross",
    "Shaunae Miller-Uibo",
    "Phyllis Francis"
]

# Initialize a counter for lap numbers
lap_number = 1

# Use a for loop to display each athlete's name along with the lap number
for athlete in athletes:
    print(f"Lap {lap_number}: {athlete} has completed their lap!")
    lap_number += 1  # Increment lap number

# Bonus: Display a message after all laps are completed
print("\nAll athletes have completed their laps!")
