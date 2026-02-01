students = [
    {"name": "Alice", "grades": [88, 92,79]},
    {"name": "Bob", "grades": [95, 70, 68]},
    {"name": "Charlie", "grades": [75, 93, 67]},
    {"name": "John", "grades": [65, 70, 58]}
]

averages = [
    {"name": student["name"], "average": round(sum(student["grades"]) / len(student["grades"]), 2)}
    for student in students
]

passing = [
    student for student in students
    if sum(student["grades"]) / len(student["grades"]) >= 75
]

sorted_by_avg = sorted(
    students, 
    key=lambda student: sum(student["grades"]) / len(student["grades"]),
    reverse=True
)

top_student = max(students, key=lambda student: sum(student["grades"]) / len(student["grades"]))

bottom_student = min(students, key=lambda student: sum(student["grades"]) / len(student["grades"]))

print(top_student)
print()
print(bottom_student)