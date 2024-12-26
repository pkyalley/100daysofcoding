# Instructions
    # Write a program that calculates and outputs the number of characters in any name. The automated tests will try out lots of different names as the input. Your code should work for any name. Your code should only output the number, no other text is needed.

# Hint
    # Remember, you can use len() around any piece of text to calculate the number of characters.
    # e.g. https://www.google.com/search?q=how+to+get+the+length+of+a+string+in+python+stack+overflow

# Important
    # Don't add prompt text to the input() function.

# e.g. use
    # ✅ name = input()

# don't use:
    # ❌ name = input("What's your name?")

# Solution

name = input()
numOfName = len(name)

print(numOfName)

# Comments
    # I used a method that takes a name as input without any prompt text.
    # The i used the function [len()] that calculates the number of characters in the name.
    # The I printed the outputs only which is the number of characters.