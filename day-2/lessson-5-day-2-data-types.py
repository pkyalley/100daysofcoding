# Instructions
    # Write a program that adds the digits in a 2 digit number.
    # e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning
    # Do not change the code on line 1. 
    # Your program should work for different inputs. e.g. any two-digit number.

# The last line of your program should print the result.

# Example 1 Input
    # 39

# Example 1 Output
    # 12

# Example 2 Input
    # 43

# Example 2 Output
    # 7

# two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

# Solution

two_digit_number = input()

num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

print(num1 + num2)

# Comments:
    # I read the input from the user and stored it in the variable two_digit_number.
    # I then extracted the first digit of the input and converted it to an integer, storing it in num1.
    # I extracted the second digit of the input and converted it to an integer, storing it in num2.
    # I now added num1 and num2 together and printed the result.