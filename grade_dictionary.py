school = { "bhawani": "A", "altair": "A", "ashar": "B", "vinay": "D", "ryan": "C" }  # Dictionary to store student names and grades.
print("Enter new student name:")
new_student = input()  # user input for new student name.
print("Enter grade for " + new_student + ":")
new_grade = input()  # Input for new student grade.
school[new_student] = new_grade  # Add new student and grade to the dictionary.
print("Enter name of existing student to update grade, write only small letters:")  # Input for existing student grade update.
existing_student = input()  # Input for existing student name.
if existing_student in school:  # Check if the student exists in the dictionary.
    print("Enter new grade for " + existing_student + ":")
    updated_grade = input()  # Input for updated grade.
    school[existing_student] = updated_grade  # Update the student's grade in the dictionary.
else:
    print("Student not found in the dictionary.")
print("Updated student grades:")
for student, grade in school.items():  # Loop through the dictionary to print all students and their grades.
    print(student + ": " + grade)  # Print each student's name and grade.
