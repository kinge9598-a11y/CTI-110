# Eddie King
# September 12, 2026
# P1HW2
# This program calculates travel expenses and shows how much money is left from the user's travel budget.

# PSEUDOCODE: 
# 1. Ask the user to enter their travel budget. 
# 2. Ask the user to enter their travel destination. 
# 3. Ask the user to enter the amount they will spend on gas. 
# 4. Ask the user to enter the amount they will spend on accommodation. 
# 5. Ask the user to enter the amount they will spend on food. 
# 6. Add the gas, accommodation, and food expenses together. 
# 7. Subtract the total expenses from the travel budget. 
# 8. Display the destination, starting budget, total expenses, and remaining budget.


# Information from the user
budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you plan to spend on gas? "))
accommodation = float(input("How much do you plan to spend on accommodation? "))
food = float(input("How much do you plan to spend on food? "))

# Calculate total expenses
total_expenses = gas + accommodation + food

# Calculate the amount left after expenses
remaining_budget = budget - total_expenses

# Display the results
print("\n----- Travel Expenses -----")
print("Travel Destination:", destination)
print("Starting Budget: $", format(budget, ".2f"))
print("Gas: $", format(gas, ".2f"))
print("Accommodation: $", format(accommodation, ".2f"))
print("Food: $", format(food, ".2f"))
print("Total Expenses: $", format(total_expenses, ".2f"))
print("Remaining Budget: $", format(remaining_budget, ".2f"))
