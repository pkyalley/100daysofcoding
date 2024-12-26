intro =(
"""
---------------------------
The Tip Calculator🧮📠💵
---------------------------
"""
)

message = """Hey there👋!
Welcome to the Tip Calculator🤗!\n"""

goodbye = (
"""
----------------------------------
Goodbye! Thank you for your tip!💵
----------------------------------
"""
)

print(intro)
print(message)

total_bill = input("What was the total bill\n")
user_percentage = input("In percentage, how much tip would you like to give? 10, 12, or 15\n")

actual_tip_percentage = float(user_percentage) / 100
tip_percentage = float(total_bill) * float(actual_tip_percentage)
people_sharing_bill = input("How many people to split the bill? Please enter number:\n")
bill_to_pay = float(total_bill) + float(tip_percentage)
amount_per_person = float(bill_to_pay) / float(people_sharing_bill)

amount_per_person_in_2_decimals = f"{amount_per_person:.2f}"


print(f"\nIncluding tip, each person should pay: ${amount_per_person_in_2_decimals}")
print(goodbye)
