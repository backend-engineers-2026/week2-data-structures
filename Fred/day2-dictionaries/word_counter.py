# Exercise 1: Word frequency counter
text = "python is great python is powerful python is fun"
# Build dict: {"python": 3, "is": 3, ...}
# Find most common word
# 1. split the words
words = text.split()
# 2. Create a dictionaly
word_counts = {}
for word in words:
    # If word Exists in dictionary, increment count
    if word in word_counts:
        word_counts[word] += 1
    # If it does not exist add it to dict
    else:
        word_counts[word] = 1
# 3. find most common word
most_common = max(word_counts.keys(), key=lambda k: word_counts.get(k, 0))
most_common_count = word_counts[most_common]

print("Words:", words)
print("Word counts:", word_counts)
print(f"Most common word: '{most_common}' ({most_common_count} times)")
