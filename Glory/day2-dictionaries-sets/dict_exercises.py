fruits = ["apple", "banana", "cherry", "apple", "orange", "cherry", "kiwi"]

frequencies = {}
for item in fruits:
    frequencies[item] = frequencies.get(item, 0) + 1

print(frequencies)

# student database
students = {
    "S001": {"name": "Alice", "grade": 85},
    "S002": {"name": "Bob", "grade": 92}
}

# - Add new student
def add_student(student_id, name, grade):
    if student_id in students:
        return "Student ID already exists"
    students[student_id] = {"name": name, "grade": grade}
    return students

# - Update grade
def update_grade():
    students["S001"].update({"grade": 88})
    return students

# - Find students with grade > 90
def find_student():
    result = []
    for number in students.keys():
        if students[number]["grade"] > 90:
            result.append({number: students[number]})
    return result

# - Use dict comprehension to create ID->name mapping
id_name_mapping = {id: student["name"] for id, student in students.items()}


print(add_student("S003", "Glory", 79))
print(update_grade())
print(find_student())
print(id_name_mapping)
