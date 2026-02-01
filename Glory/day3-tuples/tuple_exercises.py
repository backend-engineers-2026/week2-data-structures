students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("Diana", "C")
]

# Create dict to group: {"A": ["Alice", "Charlie"], ...}
grades = {}
for name, grade in students:
    if grade not in grades:
        grades[grade] = []
    grades[grade].append(name)
print("Grouped by grade:", grades)

# Count students per grade
grade_counts = {}
for name, grade in students:
    grade_counts[grade] = grade_counts.get(grade, 0) + 1
print("Count per grade:", grade_counts)
