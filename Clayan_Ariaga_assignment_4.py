"""
COMP 163 - Introduction to Programming
Assignment: Chapter 4 - College Life Adventure Game
Name: Clayan Ariaga
GitHub Username: cjariaga
Date: February 9, 2026
Description: This game simulates a student's semester by balancing course load,
study focus, and stress. Your choices change GPA, study hours, and social points
and lead to different semester endings.
AI Usage: AI was used to explain the rubric and make sure all requirement were met.
"""

# ========================================
# Step 1: Foundation Setup
# ========================================
student_name = "Clayan Ariaga"

quit_game = False

gpa_input = input("Current GPA (1.0-4.0): ")
if gpa_input.lower() == 'quit':
    quit_game = True
    current_gpa = 0.0
else:
    current_gpa = float(gpa_input)

study_hours_input = input("Study hours: ")
if study_hours_input.lower() == 'quit':
    quit_game = True
    study_hours = 0
else:
    study_hours = int(study_hours_input)

social_points_input = input("Social points: ")
if social_points_input.lower() == 'quit':
    quit_game = True
    social_points = 0
else:
    social_points = int(social_points_input)

stress_level_input = input("Stress level (0-100): ")
if stress_level_input.lower() == 'quit':
    quit_game = True
    stress_level = 0
else:
    stress_level = int(stress_level_input)

print(f"Welcome {student_name} to the College Life Game")
print("Here are your starting stats:")
print(
    f"GPA: {current_gpa}, Study Hours: {study_hours}, "
    f"Social Points: {social_points}, Stress Level: {stress_level}"
)

# ========================================
# Decision 1: Course Load Selection
# ========================================
if not quit_game:
    print("Choose your course load:")
    print("A. Light (12 credits)")
    print("B. Standard (15 credits)")
    print("C. Heavy (18 credits)")

    choice = input("Your choice: ")

    if choice in ["A", "a"]:
        if current_gpa >= 2.0 and current_gpa <= 4.0:
            study_hours += 5
            stress_level -= 5
            print("Light load: less stress, extra time to study.")
        else:
            stress_level += 5
            print("Even with a light load, low GPA will make it tough.")
    elif choice in ["B", "b"]:
        study_hours += 10
        if current_gpa != 4.0:
            stress_level += 5
        else:
            stress_level += 3
        print("Standard load: balanced but challenging.")
    elif choice in ["C", "c"]:
        if current_gpa >= 3.5:
            study_hours += 15
            stress_level += 15
            print("Heavy load with strong GPA: you manage, but it is stressful.")
        else:
            current_gpa -= 0.2
            stress_level += 25
            print("Heavy load with lower GPA: stress rises, GPA will drop.")
    else:
        print("Invalid input. Defaulting to standard load.")
        study_hours += 10
        stress_level += 5

# ========================================
# Step 3: Study Strategy Decision
# ========================================
if not quit_game:
    study_options = ["Programming", "Math", "English", "History"]
    print("Pick a subject to focus your study hours on:")
    print(study_options)
    study_choice = input("Your choice: ")

    if study_choice not in study_options:
        print("Invalid choice. No study focus selected.")
    else:
        if study_choice == "Programming" and current_gpa < 3.0:
            current_gpa += 0.3
            print("Programming focus helps raise your GPA!")
        elif study_choice == "Math" or study_choice == "English":
            current_gpa += 0.1
            social_points -= 5
            print(f"Studying {study_choice} boosted GPA but cut into your social life.")
        else:
            social_points += 5
            print(f"Studying {study_choice} gave you balance and better connections.")

# ========================================
# Step 4: Final Semester Assessment
# ========================================
print("Final Semester Assessment")

if type(current_gpa) is float:
    print("Confirmed: GPA is a float type.")
elif type(current_gpa) is not float:
    print("Invalid GPA type.")

if current_gpa >= 3.5:
    if stress_level < 50:
        if social_points >= 40:
            ending = "Dean's List with strong balance."
        else:
            ending = "Dean's List but social life suffered."
    else:
        ending = "High GPA but too stressed: burnout ending."
elif current_gpa < 2.0:
    if social_points < 30:
        if stress_level > 60:
            ending = "Complete burnout: low GPA, low support, high stress."
        else:
            ending = "Academic probation: low GPA and no support system."
    else:
        ending = "Probation, but friends keep you going."
else:
    if study_hours > 25 and stress_level < 60:
        ending = "Balanced success: steady GPA and manageable stress."
    else:
        ending = "Average semester: you stayed afloat."

print(f"Final Stats for {student_name}:")
print(
    f"GPA: {round(current_gpa, 2)}, Study Hours: {study_hours}, "
    f"Social Points: {social_points}, Stress Level: {stress_level}"
)
print(f"Ending: {ending}")
