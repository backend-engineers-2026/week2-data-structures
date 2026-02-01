# Grade calculator with statistics
# Input: List of (student_name, score) tuples
# Output:
# - Class average
# - Letter grade distribution (A, B, C, D, F)
# - Top 3 students
# Use dictionaries to count grade distribution

students = [
    ("Alice", 35),
    ("Bob", 48),
    ("Charlie", 92),
    ("John", 68),
    ("Dan", 56)
]

def class_average(data):
    total = sum(score for _, score in data)
    return round(total / len(data), 2)

def letter_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

def grade_distribution(data):
    distribution = {}

    for _, score in data:
        grade = letter_grade(score)
        distribution[grade] = distribution.get(grade, 0) + 1

    return distribution

def top_three(data):
    sorted_students = sorted(data, key=lambda x: x[1], reverse=True)
    return sorted_students[:3]

print(f"Class Average: {class_average(students)}")
print("\nGrade Distribution:")
for grade, count in grade_distribution(students).items():
    print(f"{grade}: {count}")

print("\nTop Three Students:")
for name, score in top_three(students):
    print(f"{name} - {score}")