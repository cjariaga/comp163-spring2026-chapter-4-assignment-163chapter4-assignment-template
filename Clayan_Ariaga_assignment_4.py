"""
COMP 163 - Introduction to Programming
Assignment: Chapter 4 - College Life Adventure Game
Name: Clayan Ariaga
GitHub Username: cjariaga
Date: February 9, 2026
Description: This game simulates a student's semester by balancing course load,
study focus, and stress. Your choices change GPA, study hours, and social points
and lead to different semester endings.
"""

# ========================================
# Step 1: Foundation Setup
# ========================================
student_name = "Clayan Ariaga"  # Student name displayed in game output
current_gpa = float(input("Current GPA (1.0-4.0): "))  # Float between 1.0-4.0
study_hours = int(input("Study hours: "))  # Integer (e.g., 25)
# Tracks total points earned from social activities
social_points = int(input("Social points: "))  # Integer (e.g., 50)
stress_level = int(input("Stress level (0-100): "))  # Integer 0-100

print(f"Welcome {student_name} to the College Life Game")
print("Here are your starting stats:")
print(
    f"GPA: {current_gpa}, Study Hours: {study_hours}, "
    f"Social Points: {social_points}, Stress Level: {stress_level}"
)

# ========================================
# Decision 1: Course Load Selection
# ========================================
print("Choose your course load:")
print("A. Light (12 credits)")
print("B. Standard (15 credits)")
print("C. Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    # Check if GPA is strong enough to benefit from a lighter schedule
    if current_gpa >= 2.0 and current_gpa <= 4.0:
        study_hours += 5
        stress_level -= 5
        print("Light load: less stress, extra time to study.")
    else:
        # Low GPA means even a light schedule feels hard
        stress_level += 5
        print("Even with a light load, low GPA will make it tough.")
elif choice == "B":
    # Standard load is the baseline; perfect GPA reduces stress slightly
    study_hours += 10
    if current_gpa != 4.0:
        stress_level += 5
    else:
        stress_level += 3
    print("Standard load: balanced but challenging.")
elif choice == "C":
    # Heavy load is only manageable for higher GPA students
    if current_gpa >= 3.5:
        study_hours += 15
        stress_level += 15
        print("Heavy load with strong GPA: you manage, but it is stressful.")
    else:
        current_gpa -= 0.2
        stress_level += 25
        print("Heavy load with lower GPA: stress rises, GPA will drop.")
else:
    # Invalid choice defaults to standard load
    print("Invalid input. Defaulting to standard load.")
    study_hours += 10
    stress_level += 5
