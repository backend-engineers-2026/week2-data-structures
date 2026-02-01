# Exercise 2: List comprehension challenges
numbers = range(1, 51)
# - Get all even numbers
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
# - Get squares of odd numbers
odd_numbers = [n**2 for n in numbers if n % 2]
print(odd_numbers)
# - Filter numbers divisible by both 3 and 5
numbers_divisible_by_3_and_5 = [n for n in numbers if n % 3 == 0 and n % 5 == 0]
print(numbers_divisible_by_3_and_5)
