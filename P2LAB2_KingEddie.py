# Eddie King 
# 09/24/2026 
# P2LAB2 
# This program uses a dictionary to store automobile MPG values, allows the user to select a vehicle, and calculates the gallons 
# of gas needed to drive a specified number of miles.

# Pseudocode:
# Create a dictionary containing vehicles and their MPG values 
# Get the keys from the dictionary 
# Display the available vehicles 
# Ask the user to enter a vehicle
# Display the MPG for the selected vehicle 
# Ask the user how many miles they will drive 
# Calculate gallons of gas needed 
# Display the gallons needed rounded to two decimal places

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

#Get keys from the dictionary
cars_keys = cars.keys()

print(cars_keys)

print(*cars_keys, sep = ", ")

#Get a car from the user
car_name = input("Enter a car: ")

#Get mpg for the given car
car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} miles per gallon.")

#Get miles from the user
miles_driven = float(input(f"How many miles will you drive the {car_name}?"))

#Calculate
gallons_needed = miles_driven/car_mpg

#Display results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")