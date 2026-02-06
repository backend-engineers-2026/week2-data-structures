# ============================================================================
# Exercise 1: Student grade analyzer
# ============================================================================

grades = [85, 92, 78, 90, 88, 76, 95, 89]

print("=" * 60)
print("EXERCISE 1: Student Grade Analyzer")
print("=" * 60)
print(f"Original grades: {grades}\n")

# Task 1: Find average
average = sum(grades) / len(grades)
print(f"1. Average grade: {average:.2f}")

# Task 2: Get all grades above 85
grades_above_85 = [grade for grade in grades if grade > 85]
print(f"2. Grades above 85: {grades_above_85}")

# Task 3: Count failing grades (< 70)
failing_count = len([grade for grade in grades if grade < 70])
print(f"3. Number of failing grades (< 70): {failing_count}")

# Task 4: Use comprehension to add 5 bonus points to all
bonus_grades = [grade + 5 for grade in grades]
print(f"4. Grades with 5 bonus points: {bonus_grades}")
