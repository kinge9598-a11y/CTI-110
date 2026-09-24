# Eddie King
# 09/24/2026
# P2HW1
# This program calculates the remaining travel budget after
# subtracting gas, accommodation, and food expenses.

# Pseudocode:
# Ask the user to enter their budget
# Ask the user to enter their travel destination
# Ask the user to enter the amount spent on gas
# Ask the user to enter the amount spent on accommodation
# Ask the user to enter the amount spent on food
# Calculate the total expenses
# Calculate the remaining budget
# Display the travel expenses in a formatted table

budget = float(input("Enter your budget: "))

destination = input("Enter your travel destination: ")

gas = float(input("How much do you expect to spend on gas? "))

accommodation = float(input("How much do you expect to spend on accommodation? "))

food = float(input("How much do you expect to spend on food? "))

total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses

print()
print("------------ Travel Expenses ------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${accommodation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("------------------------------------------")
print(f"{'Remaining Balance:':<20}${remaining_budget:.2f}")