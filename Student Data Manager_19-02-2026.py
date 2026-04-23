# Student Data Manager

students = {}
total = 0

# Input data for 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    total = total + marks

# Find topper
topper = max(students, key=students.get)
print("Topper:", topper)

# Class average
average = total / 5
print("Class Average:", average)

# Grades
for name in students:
    marks = students[name]

    if marks >= 90:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "D"

    print(name, "-", marks, "Grade:", grade)