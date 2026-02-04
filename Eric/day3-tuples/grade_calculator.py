def calculate_grade(score):
    """Convert score to letter grade"""
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

def grade_calculator(student_scores):
    """
    Input: List of (student_name, score) tuples
    Output: Dictionary with statistics
    """
    if not student_scores:
        return "No students provided"
    
    # Calculate class average
    total_score = sum(score for _, score in student_scores)
    class_average = total_score / len(student_scores)
    
    # Grade distribution using dictionary
    grade_dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    
    # Create list of (name, score, grade) for sorting
    detailed_scores = []
    
    for name, score in student_scores:
        grade = calculate_grade(score)
        grade_dist[grade] += 1
        detailed_scores.append((name, score, grade))
    
    # Top 3 students (sorted by score descending)
    top_3 = sorted(detailed_scores, key=lambda x: x[1], reverse=True)[:3]
    
    return {
        'class_average': round(class_average, 2),
        'total_students': len(student_scores),
        'grade_distribution': grade_dist,
        'top_3_students': [
            {'name': name, 'score': score, 'grade': grade} 
            for name, score, grade in top_3
        ]
    }

# Example usage
students_data = [
    ("Emma", 95),
    ("Liam", 87),
    ("Sophia", 92),
    ("Noah", 78),
    ("Olivia", 88),
    ("James", 45),
    ("Ava", 91),
    ("Benjamin", 82)
]

results = grade_calculator(students_data)

print("=" * 40)
print("GRADE REPORT")
print("=" * 40)
print(f"Class Average: {results['class_average']}%")
print(f"Total Students: {results['total_students']}")
print("\nGrade Distribution:")
for grade, count in results['grade_distribution'].items():
    bar = "█" * count
    print(f"  {grade}: {bar} ({count})")

print("\nTop 3 Students:")
for i, student in enumerate(results['top_3_students'], 1):
    print(f"  {i}. {student['name']}: {student['score']}% ({student['grade']})")