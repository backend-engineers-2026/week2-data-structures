# # Exercise 1: Student grade analyzer
# grades = [85, 92, 78, 90, 88, 76, 95, 89]

# # Task 1: Find average
# average = sum(grades) / len(grades)
# print(f"Average: {average}")

# # Task 2: Get all grades above 85
# above_85 = [grade for grade in grades if grade > 85]
# print(f"Grades above 85: {above_85}")

# # Task 3: Count failing grades (< 70)
# failing_count = len([grade for grade in grades if grade < 70])
# print(f"Failing grades count: {failing_count}")

# # Task 4: Use comprehension to add 5 bonus points to all
# with_bonus = [grade + 5 for grade in grades]
# print(f"Grades with +5 bonus: {with_bonus}")

# unrelated, but the output is ['America', 'Australia', 'Chile']
# countries = ["America", "Canada", "Australia", "China", "Chile"]
# for c in countries:
#     if c.startswith("C"):
#         countries.remove(c) # ["America", "Australia", "Chile"]
# print(countries)

countries = ["America", "Canada", "Australia", "China", "Chile"]
filtered_countries = [c for c in countries if not c.startswith("C")]

print(filtered_countries)