# Task 2: Computing Body Mass Index (BMI)

"""
Write a python program to compute body mass index (BMI). The program should take input values such as weight and height in order to calculate BMI and display it on the screen. In addition, the program should display to the user whether the calculated BMI result corresponds to underweight, healthy weight, or overweight.
Formula: weight (kg) / [height (m)]^2
"""

# Prompt the user to input height and weight
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# Calculate BMI using the provided formula
BMI = weight / (height/100)**2

# Check the calculated BMI and provide corresponding output based on the value
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are overweight.")
elif BMI <= 34.9:
    print("You are severely overweight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")