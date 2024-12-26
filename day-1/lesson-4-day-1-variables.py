# Instructions
    # This program takes two inputs.
    # The first input is stored in a variable called a.
    # The second input is stored in a variable called b.

# Write a program that switches the values stored in the variables a and b.

# Warning
    # You don't need to print anything. 
    # The print statement is already in the template code. 
    # However, your program should work for different inputs. e.g. any value of a and b.

# Example Input 1
    # 29
    # 41
# Example Output 1
    # a: 41
    # b: 29

# Example Input 2
    # Hello
    # World
# Example Output 2
    # a: World
    # b: Hello

# There are two variables, a and b from input
# a = input()
# b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇


# 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)

# Solution

a = input()
b = input()

change1 = a
change2 = b

a = change2
b = change1

print("a: " + a)
print("b: " + b)

# Comment
    # I stored the input values in a and b.
    # I now used temporary variables to swap the values.
    # Then I printed the swapped values.

# Improved Method

a = input()
b = input()

temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)
