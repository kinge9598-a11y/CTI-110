# Eddie King
#10/15/2026
#P4HW2
#Salary Calculator with loops

# Pseudocode:
# 1. Ask for employee name.
# 2. Calculate regular pay, overtime pay, and gross pay.
# 3. Display employee pay and update totals.
# 4. Repeat until the user enters done.
# 5. Display final totals.



# request employee info
name = input("Enter employee's name or 'done' to finish: ")

# Create accumulator variables
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'done':
    employee_count += 1

    # Ask for employee info
    hours = float(input("How many hours did " + name + " work this week? "))
    rate = float(input("What is " + name + "'s hourly pay rate? "))

    # Evaluate overtime
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        regular_pay = hours * rate
        gross_pay = regular_pay

    # Add pay to totals
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

    # Display results for this employee
    print("----------------------------------------------")
    print("Employee Name:", name)
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}')
    print("--------------------------------------------------------------------------")
    print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}')

    name = input("Enter employee's name or 'done' to finish: ")

# Display final totals
print("Total number of employees entered:", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular time: $", format(regularpay_total, ',.2f'))
print("Total amount paid in gross: $", format(grosspay_total, ',.2f'))

        