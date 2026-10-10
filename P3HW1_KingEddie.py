
# Eddie King
# October 10, 2026
# P3HW1 - Debugging
# This program collects six grades and displays the lowest grade,highest grade,  sum, average, and letter grade.

# Pseudocode:
# Ask the user to enter six grades.
# Store the grades in a list.
# Find the lowest and highest grades.
# Calculate the sum and average of the grades.
# Determine the letter grade based on the average.
# Display the results.
# This program takes six module grades, determines the average,
# and displays the lowest, highest, sum, average, and letter grade.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

print()
print(f'Lowest grade: {low:g}')
print(f'Highest grade: {high:g}')
print(f'Sum of grades: {total:g}')
print(f'Average: {avg:.2f}')

# Determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
