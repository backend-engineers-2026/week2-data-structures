# ============================================================================
# EXERCISE 1: Word Counter
# ============================================================================

print("=" * 70)
print("EXERCISE 1: Word Frequency Counter")
print("=" * 70)

text = "python is great python is powerful python is fun"
print(f"Original text: '{text}'\n")

# Method 1: Using a loop
word_freq = {}
words = text.split()

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("1. Word frequency dictionary:")
print(word_freq)

# Find most common word
most_common_word = max(word_freq, key=word_freq.get)
max_count = word_freq[most_common_word]
print(f"\n2. Most common word: '{most_common_word}' (appears {max_count} times)")

# Method 2: Using get() method (more elegant)
word_freq_v2 = {}
for word in words:
    word_freq_v2[word] = word_freq_v2.get(word, 0) + 1

print(f"\n3. Using get() method: {word_freq_v2}")

# Method 3: Using Counter from collections (most Pythonic)
from collections import Counter
word_freq_v3 = Counter(words)
print(f"\n4. Using Counter: {dict(word_freq_v3)}")
print(f"   Most common: {word_freq_v3.most_common(1)}")

# Bonus: All words sorted by frequency (descending)
sorted_by_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
print(f"\n5. Words sorted by frequency:")
for word, count in sorted_by_freq:
    print(f"   '{word}': {count}")