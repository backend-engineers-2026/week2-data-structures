# ============================================================================
# EXERCISE 2: Student Database
# ============================================================================

print("\n" + "=" * 70)
print("EXERCISE 2: Student Database")
print("=" * 70)

students = {
    "S001": {"name": "Alice", "grade": 85},
    "S002": {"name": "Bob", "grade": 92}
}

print("\n1. Original student database:")
for student_id, info in students.items():
    print(f"   {student_id}: {info['name']} - Grade: {info['grade']}")

# Task 1: Add new student
print("\n2. Adding new student (Charlie):")
students["S003"] = {"name": "Charlie", "grade": 88}
print(f"   Added: S003 - {students['S003']}")

# Task 2: Update grade
print("\n3. Updating Alice's grade from 85 to 90:")
students["S001"]["grade"] = 90
print(f"   Updated: S001 - {students['S001']}")

# Task 3: Find students with grade > 90
print("\n4. Students with grade > 90:")
high_performers = {
    student_id: info 
    for student_id, info in students.items() 
    if info["grade"] > 90
}
for student_id, info in high_performers.items():
    print(f"   {student_id}: {info['name']} - Grade: {info['grade']}")

# Alternative method using filter
print("\n5. Alternative method using filter:")
high_performers_list = list(filter(lambda x: x[1]["grade"] > 90, students.items()))
for student_id, info in high_performers_list:
    print(f"   {student_id}: {info['name']} - Grade: {info['grade']}")

# Task 4: Create ID->name mapping using dict comprehension
print("\n6. ID to Name mapping (using dict comprehension):")
id_to_name = {student_id: info["name"] for student_id, info in students.items()}
print(f"   {id_to_name}")

# Bonus: More dict comprehensions
print("\n7. BONUS - More dictionary comprehensions:")

# Grade to Name mapping
grade_to_name = {info["grade"]: info["name"] for info in students.values()}
print(f"   Grade to Name: {grade_to_name}")

# Create uppercase name mapping
upper_names = {student_id: info["name"].upper() for student_id, info in students.items()}
print(f"   Uppercase names: {upper_names}")

# Filter and transform: students with grade >= 90, names only
top_students = {
    student_id: info["name"] 
    for student_id, info in students.items() 
    if info["grade"] >= 90
}
print(f"   Top students (grade >= 90): {top_students}")

# Calculate statistics
print("\n8. Student Statistics:")
all_grades = [info["grade"] for info in students.values()]
print(f"   Average grade: {sum(all_grades) / len(all_grades):.2f}")
print(f"   Highest grade: {max(all_grades)}")
print(f"   Lowest grade: {min(all_grades)}")
print(f"   Total students: {len(students)}")


# ============================================================================
# EXERCISE 3: Set Operations
# ============================================================================

print("\n" + "=" * 70)
print("EXERCISE 3: Set Operations")
print("=" * 70)

team_a = {"Alice", "Bob", "Charlie"}
team_b = {"Bob", "Diana", "Eve"}

print(f"\nTeam A: {team_a}")
print(f"Team B: {team_b}")

# Task 1: Common members (intersection)
print("\n1. Common members (intersection):")
common = team_a & team_b  # or team_a.intersection(team_b)
print(f"   Using &: {common}")
print(f"   Using .intersection(): {team_a.intersection(team_b)}")

# Task 2: All members (union)
print("\n2. All members (union):")
all_members = team_a | team_b  # or team_a.union(team_b)
print(f"   Using |: {all_members}")
print(f"   Using .union(): {team_a.union(team_b)}")

# Task 3: Unique to team_a (difference)
print("\n3. Unique to Team A (difference):")
unique_a = team_a - team_b  # or team_a.difference(team_b)
print(f"   Using -: {unique_a}")
print(f"   Using .difference(): {team_a.difference(team_b)}")

# Bonus: More set operations
print("\n4. BONUS - Additional Set Operations:")

# Unique to team_b
unique_b = team_b - team_a
print(f"   Unique to Team B: {unique_b}")

# Symmetric difference (members in either team but not both)
symmetric_diff = team_a ^ team_b  # or team_a.symmetric_difference(team_b)
print(f"   In either team but not both: {symmetric_diff}")

# Check if team_a is a subset of combined teams
combined = team_a | team_b
is_subset = team_a.issubset(combined)
print(f"   Is Team A a subset of combined? {is_subset}")

# Check if teams are disjoint (no common members)
are_disjoint = team_a.isdisjoint(team_b)
print(f"   Are teams disjoint (no overlap)? {are_disjoint}")

# Practical example: Team assignments
print("\n5. Practical Example - Team Assignments:")
print(f"   Members in both teams (need to choose): {common}")
print(f"   Members only in Team A: {unique_a}")
print(f"   Members only in Team B: {unique_b}")
print(f"   Total unique members: {len(all_members)}")
