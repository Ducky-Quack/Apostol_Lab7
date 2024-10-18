name = input("What is your name?\n")
section = input("What is your section? (ex. IT-101)\n")

prelim = float(input("What is your preliminary grade: "))
midterm = float(input("What is your midterm grade: "))
final = float(input("What is your final grade: "))

# Checking for each grade condition
while not (40 <= prelim <= 100) or not (40 <= midterm <= 100) or not (40 <= final <= 100):
    print("\nYou have inputted an invalid number(s).")
    if not (40 <= prelim <= 100):
        prelim = float(input("Please enter your PRELIMINARY grade again.\nPreliminary grade: "))
    if not (40 <= midterm <= 100):
        midterm = float(input("Please enter your MIDTERM grade again.\nMidterm grade: "))
    if not (40 <= final <= 100):
        final = float(input("Please enter your FINAL grade again.\nFinal grade: "))

# Final grade computation
final_grade = round((prelim * 0.33) + (midterm * 0.33) + (final * 0.33) + 1)

# Check for grade points AND general description
if final_grade >= 99:
    GPA, description = 1.00, "Excellent"
elif final_grade >= 96:
    GPA, description = 1.25, "Outstanding"
elif final_grade >= 93:
    GPA, description = 1.50, "Superior"
elif final_grade >= 90:
    GPA, description = 1.75, "Very Good"
elif final_grade >= 87:
    GPA, description = 2.00, "Good"
elif final_grade >= 84:
    GPA, description = 2.25, "Satisfactory"
elif final_grade >= 81:
    GPA, description = 2.50, "Fairly Satisfactory"
elif final_grade >= 78:
    GPA, description = 2.75, "Fair"
elif final_grade >= 75:
    GPA, description = 3.00, "Passed"
else:
    GPA, description = 5.00, "Failed"

# Print final grade, GPA, and description
print(f"\nHello, {name} (from {section})!")
print(f"Your final grade is: {final_grade}%")
print(f"Your GPA is {GPA} ({description})\n")
