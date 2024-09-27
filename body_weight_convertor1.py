# 1lbs = 0.453592

weight_in_lbs = float(input("Enter your weight in pounds: \n"))
weight_in_kg = weight_in_lbs * 0.453592

# This will round the output to 2 decimal places.
print(f"Your weight in kilograms is: {weight_in_kg: .2f}")