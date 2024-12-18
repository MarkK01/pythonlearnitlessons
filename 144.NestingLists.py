# Create dictionary to store student information
student_1 = {
    "name": "Alice",
    "age": 20,
    "courses": [
        {
            "course_name": "Math",
            "grade": "A"
        },
        {
            "course_name": "History",
            "grade": "B"
        }
    ]
}

student_2 = {
    "name": "Bob",
    "age": 22,
    "courses": [
        {
            "course_name": "Physics",
            "grade": "B"
        },
        {
            "course_name": "English",
            "grade": "A"
        }
    ]
}

# List of students
students = [student_1, student_2]

# Print student information
for student in students:
    print(f"Student: {student['name']}")
    print(f"Age: {student['age']}")