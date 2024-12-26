intro =(
"""
-------------------------------
The Band Name Generator 🎸🎹🎻
-------------------------------
"""
)

message = """Hey there👋!
Welcome to the Band Name Generator🥳!\n"""

goodbye = (
"""
----------------------------------
Goodbye! Go make good music🎸🎹🎻
----------------------------------
"""
)

print(intro)
print(message)

userName = input("What is your name?\n")
petName = input("What is the name of your pet?\n")
cityName = input("Which city did you grow up in?\n")
bandNameAbbreviation = f"{userName[0].title()}{petName[0].title()}{cityName[0].title()}"

print(f"\nYour band name could be: {str(userName.title())} {str(petName.title())} {str(cityName.title())} - ({bandNameAbbreviation})")
print(goodbye)
