# ==========================================
# Exercise 1: Manual CSV Parser
# ==========================================

def parse_csv_manual(filename):
    """
    Manually parse CSV file without using csv module
    Demonstrates: split(), strip(), int conversion, list comprehension
    """
    students = []
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # Extract header (first line)
    header = lines[0].strip().split(',')
    print(f"Header: {header}\n")
    
    # Parse data rows (skip header)
    for line in lines[1:]:
        line = line.strip()  # Remove \n and whitespace
        if not line:  # Skip empty lines
            continue
            
        parts = line.split(',')  # Split by comma
        
        # Create dictionary for each student
        student = {
            'name': parts[0].strip(),
            'grade': int(parts[1].strip()),  # Convert to int
            'age': int(parts[2].strip())     # Convert to int
        }
        students.append(student)
    
    return students

# Parse the file
students = parse_csv_manual('students.txt')

# Display parsed data
print("Parsed Students:")
for s in students:
    print(f"  {s['name']}: Grade={s['grade']}, Age={s['age']}")

# Calculate average grade
grades = [s['grade'] for s in students]
average_grade = sum(grades) / len(grades)
print(f"\n Average Grade: {average_grade:.2f}")

# Find students with grade > 85
high_achievers = [s for s in students if s['grade'] > 85]
print(f"\n High Achievers (Grade > 85):")
for s in high_achievers:
    print(f"  • {s['name']}: {s['grade']}")

# Find oldest student
oldest = max(students, key=lambda x: x['age'])
print(f"\n Oldest Student: {oldest['name']} ({oldest['age']} years)")