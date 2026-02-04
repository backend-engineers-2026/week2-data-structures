# ============================================================================
# Exercise 2: List comprehension challenges
# ============================================================================

numbers = range(1, 51)

print("\n" + "=" * 60)
print("EXERCISE 2: List Comprehension Challenges")
print("=" * 60)
print(f"Working with numbers from 1 to 50\n")

# Task 1: Get all even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"1. Even numbers: {even_numbers}")

# Task 2: Get squares of odd numbers
odd_squares = [num ** 2 for num in numbers if num % 2 != 0]
print(f"2. Squares of odd numbers: {odd_squares}")

# Task 3: Filter numbers divisible by both 3 and 5
divisible_by_3_and_5 = [num for num in numbers if num % 3 == 0 and num % 5 == 0]
print(f"3. Numbers divisible by both 3 and 5: {divisible_by_3_and_5}")
