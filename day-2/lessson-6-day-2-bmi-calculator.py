# Instructions
    # Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
    # BMI Wikipedia Page (https://en.wikipedia.org/wiki/Body_mass_index)

    # The BMI is a measure of someone's weight taking into account their height.
    # e.g. If a tall person and a short person both weigh the same amount,
    # the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
    # The BMI is defined as the body mass divided by the square of the body height,
    # and is expressed in units of kg/m2, resulting from mass in kilograms (kg) and height in metres (m).

# NOTE
    # You should convert the bmi to a whole number and print out a whole number in order to pass all the tests. See examples below.

# Example Input 1
    # 1.75
    # 80
    # means: weight = 80 and height = 1.75

# Example Output 1
    # 26
    # Since: 80 ÷ (1.75 x 1.75) = 26.122448979591837

# Example Input 2
    # 1.58
    # 57
# Example Output 1
    # 22

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Solution

floatHeight = float(height)
floatWeight = float(weight) 

bmi = floatWeight/floatHeight**2

result = int(bmi)

print(result)

# Comment:
    # I read the user's height and weight as input and stored them in the variables height and weight.
    # I converted the height and weight from strings to floats and stored them in floatHeight and floatWeight.
    # I calculated the BMI using the formula weight / (height ** 2).
    # I converted the BMI to an integer and stored it in result.
    # I printed the result.