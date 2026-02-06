# Create students.txt
with open("students.txt", "w") as f:
    f.write("name,grade,age\nAlice,85,20\nBob,92,21\nCharlie,78,22\nDiana,95,23")

# Read and parse
with open("students.txt", "r") as f:
    lines = f.readlines()[1:]  # Skip header

grades = []
high_achievers = []

for line in lines:
    name, grade, age = line.strip().split(",")
    grade_val = int(grade)
    grades.append(grade_val)
    if grade_val > 85:
        high_achievers.append(name)

avg_grade = sum(grades) / len(grades)
print(f"Average Grade: {avg_grade}")
print(f"Students with grade > 85: {', '.join(high_achievers)}")
