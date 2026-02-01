# Grade calculator with statistics

# Input: list of (student_name, score)
students = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 90),
    ("Diana", 66),
    ("Eve", 58),
    ("Frank", 95),
]

# 1. Class average

total_score = 0

for name, score in students:  # tuple unpacking
    total_score += score  # Add each student’s score to the total

class_average = total_score / len(students)

# 2. Letter grade distribution

grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for name, score in students:
    if score >= 90:
        grade_distribution["A"] += 1
    elif score >= 80:
        grade_distribution["B"] += 1
    elif score >= 70:
        grade_distribution["C"] += 1
    elif score >= 60:
        grade_distribution["D"] += 1
    else:
        grade_distribution["F"] += 1

# 3. Top 3 students

# Sort students by score (highest first)
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)

top_3_students = sorted_students[:3]  # Slice the first 3 items

# Output

print("Class average:", class_average)
print("Grade distribution:", grade_distribution)
print("Top 3 students:", top_3_students)
