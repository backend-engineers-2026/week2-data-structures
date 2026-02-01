# Exercise 1: Student grade analyzer
grades = [85, 92, 78, 90, 88, 76, 95, 89]
# Tasks:
# - Find average - total sum/length
average_grade = sum(grades) / len(grades)
print(average_grade)
# - Get all grades above 85
above_85 = []
for grade in grades:
    if grade > 85:
        above_85.append(grade)
print(above_85)
# - Count failing grades (< 70)
failing_grades = 0
for grade in grades:
    if grade < 70:
        failing_grades += 1
print(failing_grades)
# - Use comprehension to add 5 bonus points to all
new_grades = [g + 5 for g in grades]
print(new_grades)
