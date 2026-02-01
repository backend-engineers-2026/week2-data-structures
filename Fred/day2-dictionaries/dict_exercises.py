# Exercise 2: Student database
students = {
    "S001": {"name": "Alice", "grade": 85},
    "S002": {"name": "Bob", "grade": 92},
}
# - Add new student
students["S003"] = {"name": "Charlie", "grade": 78}
# - Update grade
students["S001"]["grade"] = 88
# - Find students with grade > 90
top_students = {sid: data for sid, data in students.items() if data["grade"] > 90}
# - Use dict comprehension to create ID->name mapping
id_to_name = {sid: data["name"] for sid, data in students.items()}

print("Students:", students)
print("Top students (grade>90):", top_students)
print("ID -> name mapping:", id_to_name)


# Exercise 3: Set operations
team_a = {"Alice", "Bob", "Charlie"}
team_b = {"Bob", "Diana", "Eve"}
# Find: common members, all members, unique to team_a
common_members = team_a & team_b  # intersection keeps only the duplicates
all_members = team_a | team_b  # union for only sets
unique_to_team_a = team_a - team_b  # difference Frozen net

print("Common members:", common_members)
print("All members:", all_members)
print("Unique to team A:", unique_to_team_a)
