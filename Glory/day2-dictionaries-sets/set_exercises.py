x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)

print(z)

# the update() method inserts all items from one set into another.
# it changes the original set, and does not return a new set
set_1 = {"a", "b", "c"}
set_2 = {1, 2, 3}

set_1.update(map(str, set_2))
print(set_1)

# the intersection() keeps only duplicates (items presents in both sets)
fruits = {"apple", "banana", "cherry"}
companies = {"google", "microsoft", "apple"}

duplicates = fruits.intersection(companies)
print(duplicates)

# the intersection_update() keeps only duplicates, but changes the original set instead of returning a new set
fruits = {"apple", "banana", "cherry"}
companies = {"google", "microsoft", "apple"}

fruits.intersection_update(companies)
print(fruits)

# the values True and 1 are considered the same value. the same goes for False and 0
set_1 = {"apple", 1, "banana", 0, "cherry"}
set_2 = {False, "google", 1, "apple", 2, True}
set_3 = set_1.intersection(set_2)
print(set_3)

# the difference() method will return a new set containing only the from the first set that are not present in the other set
fruits = {"apple", "banana", "cherry"}
companies = {"google", "microsoft", "apple"}
diff = fruits.difference(companies)
print(diff)

# the difference_update() keeps the items from the first set that are not present in the other set, but it will change the original set instead of returning a new set
fruits = {"apple", "banana", "cherry"}
companies = {"google", "microsoft", "apple"}
fruits.difference_update(companies)
print(fruits)

# the symmetric_difference() will keep only the elements that are NOT present in both sets
fruits = {"apple", "banana", "cherry"}
companies = {"google", "microsoft", "apple"}
set_3 = fruits.symmetric_difference(companies)
print(set_3)

# # the symmetric_difference_update() will also keep all but the duplicates, but it will change set instead of returning a new set
fruits = {"apple", "banana", "cherry"}
companies = {"google", "microsoft", "apple"}
fruits.symmetric_difference_update(companies)
print(fruits)

# frozenset is an immutable version of a set.
# unlike sets, elements cannot be added or removed from a frozenset
# use the frozenset() constructor to create a frozenset from any iterable
immutable_set = frozenset(["apple", "banana", "cherry"])
print(immutable_set)
print(type(immutable_set))
