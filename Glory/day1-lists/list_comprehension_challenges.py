numbers = range(1, 51)

def get_even():
    even = [num for num in numbers if num % 2 == 0]
    return even

def get_odd_square():
    squares = [num ** 2 for num in numbers if num % 2 != 0]
    return squares

# without list comprehension
# def get_odd_square():
#     squares = []
#     for num in numbers:
#         if num % 2 != 0:
#             squares.append(num ** 2)
#     return squares

def divisible():
    divisible_by_three_five = [num for num in numbers if num % 3 == 0 and num % 5 == 0]
    return divisible_by_three_five

print(get_odd_square())
print(divisible())