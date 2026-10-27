
# Eddie King
# 10/26/2026
# P4HW1 - Scores and Grades
# This program collects scores, validates them, drops the lowest score,
# calculates the average, and displays the letter grade.

# Pseudocode:
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list to store valid scores.
# 3. Use a loop to collect each score.
# 4. Check whether each score is between 0 and 100.
# 5. If the score is invalid, display an error message and ask again.
# 6. If the score is valid, add it to the score list.
# 7. After collecting all scores, find the lowest score.
# 8. Remove the lowest score from the list.
# 9. Calculate the average of the modified list.
# 10. Determine the letter grade based on the average.
# 11. Display the lowest score, modified list, average, and letter grade.
# 12. End the program.

# Ask how many scores the user wants to enter
num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list for the scores
scores = []

# Collect scores from the user
for item in range(num_scores):
    score = float(input(f"Enter score #{item + 1}: "))

    # Validate the score
    while score < 0 or score > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{item + 1} again: "))

    # Add valid score to the list
    scores.append(score)

# Find the lowest score
lowest_score = min(scores)

# Create a modified list without the lowest score
modified_scores = scores.copy()
modified_scores.remove(lowest_score)

# Calculate the average of the modified list
average_score = sum(modified_scores) / len(modified_scores)

# Determine the letter grade
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the results
print()
print("---------------Results---------------")
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {letter_grade}")
print("-------------------------------------")
